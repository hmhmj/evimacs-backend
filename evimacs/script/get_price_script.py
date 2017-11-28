# -*- coding:utf-8 -*-
import re

import datetime
import requests
from pyquery import PyQuery as pq

from evimacs.app import create_app
from evimacs.extensions import db
from evimacs.price.models import ErShouFangModel
from evimacs.utils import headers


def process():
    url = 'http://sh.lianjia.com/ershoufang/d%ss7'
    datas = list()
    for page in range(1, 200):
        response = requests.get(url % page, headers=headers)
        d = pq(response.text)
        for x in d('ul.js_fang_list li'):
            data = dict()
            x = pq(x)
            data['crawl_date'] = datetime.datetime.utcnow()
            data['prop_title'] = x('div.prop-title > a').text()
            data['prop_tag'] = x('.prop-title .c-prop-tag--blue').text()
            info = x('div.info-table span.row1-text').text().split('|')
            data['total_price'] = x('div.info-table .total-price').text() + x('div.info-table .unit').text()
            data['key'] = x('div.prop-title > a').attr('key')
            data['house_type'] = info[0].strip() if len(info) >= 1 else ''
            data['area'] = float(info[1].replace('平','').strip()) if len(info) >= 2 else 0
            floor_info = info[2] if len(info)>= 3 else ''
            if '地上' in floor_info:
                data['floor_area'] = '低区'
                data['floor_count'] = int(re.sub('(地|上|层|\n|\t|\s)','', floor_info))
            elif floor_info:
                data['floor_area'] = floor_info.split('/')[0].strip()
                data['floor_count'] = int(re.sub('(层|\n|\t|\s)','' ,floor_info.split('/')[1]))

            data['direction'] = info[3].strip() if len(info) >= 4 else ''
            data['price'] = x('div.info-table .info-row span.minor').text().strip('单价/平')
            info_ele = x('div.info-table .row2-text')
            data['position'] = info_ele('a').eq(0).text()
            data['area_name'] = info_ele('a').eq(1).text()
            build_date = info_ele.not_('a').text()
            data['build_date'] = int(re.findall('(\d+).*?年建', build_date)[0]) if re.search('(\d+).*年建', build_date) else 0
            for x in data:
                if isinstance(data[x], str):
                    data[x] = re.sub("(\n|\t)", "", data[x])

            for key in ['price', 'total_price']:
                price = data[key]
                price_count = 1
                if '千万' in price:
                    price_count = 10000000
                elif '百万' in price:
                    price_count = 1000000
                elif '十万' in price:
                    price_count = 100000
                elif '万' in price:
                    price_count = 10000
                price = price.strip('十百千万元 ')
                if not price:
                    price = 0
                data[key] = int(price) * price_count
            data['fang_type'] = 'ershoufang'
            data['deal_type'] = 0
            datas.append(data)
    for data in datas:
        price = ErShouFangModel(**data)
        db.session.add(price)
    db.session.commit()


def run():
    app = create_app()
    with app.app_context():
        process()

if __name__ == '__main__':
    run()

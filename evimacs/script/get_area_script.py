# -*- coding:utf-8 -*-
import json

import datetime
import requests

from evimacs.app import create_app
from evimacs.extensions import db
from evimacs.area.models import Area
from evimacs.utils import headers


def process():
    data = {'access_token': '7poanTTBCymmgE0FOn1oKp', 'client': 'pc', 'cityCode': 'sh', 'siteType': 'quyu',
            'type': 'district','dataId': 'sh', 'showType': 'list', 'limit_count': '2000'}

    url = 'http://soa.dooioo.com/api/v4/online/house/ershoufang/listMapResult?'

    datas = list()
    for _type in ['district', 'line']:
        data['type'] = _type
        response = requests.get(url, params=data, headers=headers)

        for x in response.json()['dataList']:
            data1 = dict()
            data1['area'] = x['showName']
            data1['area_id'] = x['dataId']
            data1['sub_area'] = ''
            data1['sub_area_id'] = ''
            data1['crawl_date'] = datetime.datetime.utcnow() - datetime.timedelta(days=1)
            data1['lat'] = x.get('lat', 0)
            data1['long'] = x.get('long', 0)
            data1['saleTotal'] = x['saleTotal']
            data1['saleAvgPrice'] = x.get('saleAvgPrice', 0)
            data1['dealAvgPrice'] = x['dealAvgPrice']
            data1['area_type'] = _type

            data['dataId'] = x['dataId']
            if _type == 'line':
                data['siteType'] = 'ditie'
                data['type'] = 'stop'
            else:
                if 'siteType' in data:
                    data.pop('siteType')
                data['type'] = 'plate'
            response = requests.get(url, params=data, headers=headers)
            datas.append(data1)
            if x['showName'] == '浦东':
                print(response.url)
            for j in response.json()['dataList']:
                data1 = dict()
                data1['area'] = x['showName']
                data1['area_id'] = x['dataId']
                data1['sub_area'] = j.get('showName', '')
                data1['sub_area_id'] = j.get('dataId', '')
                data1['crawl_date'] = datetime.datetime.utcnow()
                data1['lat'] = j.get('latitude',0)
                data1['long'] = j.get('longitude',0)
                data1['saleTotal'] = j.get('saleTotal', 0)
                data1['saleAvgPrice'] = j.get('saleAvgPrice',0)
                data1['dealAvgPrice'] = j['dealAvgPrice']
                data1['area_type'] = _type
                datas.append(data1)
    for data in datas:
        area = Area(**data)
        db.session.add(area)
    db.session.commit()

def run():
    app = create_app()
    with app.app_context():
        process()

if __name__ == '__main__':
    run()

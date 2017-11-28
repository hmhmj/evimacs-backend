# -*- coding:utf-8 -*-
from flask import request
from flask_restful import Resource

from evimacs.area.models import Area
from evimacs.extensions import api, db


@api.route("/")
class Index(Resource):
    def get(self):
        return {"liu": "dongsheng"}


@api.route("/api/get_area")
class AreaApi(Resource):
    def get(self):
        query = db.session.query(Area.area_id, Area.area, Area.area_type).filter(Area.area_type == 'district').filter(
            Area.sub_area == '').all()
        ret_item = dict()
        total = 0
        for item in query:
            if item.area_type in ret_item:
                total += 1
                ret_item[item.area_type].append({"area": item.area, "area_id": item.area_id})
            else:
                ret_item[item.area_type] = [{"area": item.area, "area_id": item.area_id}]
                total += 1
        ret_item['total'] = total
        return ret_item


@api.route("/api/area/get_agg")
class AreaAggApi(Resource):
    def get(self):
        params = request.args
        date_range = params.get('date_range', '')

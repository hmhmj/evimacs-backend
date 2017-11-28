# -*- coding:utf-8 -*-
import datetime

from evimacs.extensions import db


class Area(db.Model):
    __tablename__ = 'area'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(255), default='')
    area_id = db.Column(db.String(100))
    area_type = db.Column(db.String(255))
    sub_area = db.Column(db.String(255), default='')
    sub_area_id = db.Column(db.String(100))
    crawl_date = db.Column(db.Date, default=datetime.datetime.utcnow)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    saleTotal = db.Column(db.Integer)
    saleAvgPrice = db.Column(db.Integer)
    dealAvgPrice = db.Column(db.Integer)

    # def __init__(self, area=None, area_type=None, area_id=None, sub_area=None, sub_area_id=None, crawl_date=None,
    #              lat=None, long=None, saleTotal=None, saleAvgPrice=None, dealAvgPrice=None):
    #     self.area = area
    #     self.area_type = area_type
    #     self.area_id = area_id
    #     self.sub_area = sub_area
    #     self.sub_area_id = sub_area_id
    #     self.crawl_date = crawl_date
    #     self.lat = lat
    #     self.long = long
    #     self.saleTotal = saleTotal
    #     self.saleAvgPrice = saleAvgPrice
    #     self.dealAvgPrice = dealAvgPrice

# -*- coding:utf-8 -*-

from evimacs.extensions import db


class ErShouFangModel(db.Model):
    __tablename__ = 'price'
    prop_title = db.Column(db.Text)
    prop_tag = db.Column(db.Text)
    total_price = db.Column(db.Integer)
    key = db.Column(db.String(100))
    house_type = db.Column(db.String(100))
    area = db.Column(db.Float)
    floor_area = db.Column(db.String(100))
    floor_count = db.Column(db.Integer)
    direction = db.Column(db.String(100))
    price = db.Column(db.Integer)
    position = db.Column(db.String)
    area_name = db.Column(db.String)
    build_date = db.Column(db.Integer)
    crawl_date = db.Column(db.Date)
    id = db.Column(db.Integer, primary_key=True)
    fang_type = db.Column(db.String(100))
    deal_type = db.Column(db.Integer)
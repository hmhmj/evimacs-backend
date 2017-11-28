#!/usr/bin/env bash
#/bin/bash
export COLOREDLOGS_LOG_FORMAT='%(asctime)s %(hostname)s %(name)s[%(funcName)s]-%(levelname)s Line:%(lineno)s  %(message)s'
export FLASK_APP='./autoapp.py'
export FLAKS_DEBUG=1
#flask db init
#flask db migrate
#flask db upgrade
flask run -h0.0.0.0 -p5001

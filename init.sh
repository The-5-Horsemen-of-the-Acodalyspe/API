#!/bin/sh
#rm app.db
#python3.7 -m flask db init
#python3.7 -m flask db migrate
#python3.7 -m flask db upgrade
nohup python3.7 -m flask run &

#!/bin/sh
rm app.db
rm -r migrations
pip3 install -r requirement.txt
python3.7 -m flask db init
python3.7 -m flask db migrate
python3.7 -m flask db upgrade
nohup python3.7 -m flask run $

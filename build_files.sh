#!/bin/bash
echo "BUILD START"
python3.9 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear  
echo "BUILD END"

#! /bin/bash

# for uwsgi temp files
mkdir tmp

# for python virtual environment on linux
python3 -m venv env
source ./env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --upgrade
deactivate

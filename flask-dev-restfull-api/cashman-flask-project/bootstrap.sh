#!/bin/sh
export FLASK_APP=./cashman/app.py
pipenv run flask --debug run -h 0.0.0.0 -p 105
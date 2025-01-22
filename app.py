#!/usr/bin/env python3

import flask
from flask import render_template, request
from werkzeug.routing import BaseConverter, ValidationError


app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

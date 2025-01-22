#!/usr/bin/env python3

import os
import tomllib
import requests
import flask
from flask import render_template


app = flask.Flask(__name__)


# Load configuration from TOML file
__dir__ = os.path.dirname(__file__)
with open(os.path.join(__dir__, 'config.toml'), 'rb') as f:
    app.config.update(tomllib.load(f))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lookup/<name>')
def lookup(name):
    response = requests.post('https://phabricator.wikimedia.org/api/phid.lookup', data={
        'api.token': app.config['TOKEN'],
        'names[]': [name]
    })
    response.raise_for_status()

    json = response.json()
    if json.get('error_code'):
        return json
    result = response.json().get('result', {})
    if len(result) == 0:
        return {}
    obj = result.get(name)
    return obj

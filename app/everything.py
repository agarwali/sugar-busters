import os

# We need a bunch of Flask stuff
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import json
from flask import url_for
from flask import g
from flask import session
from flask import jsonify
from flask import send_from_directory
from flask.ext.login import LoginManager

# Some Local Stuff we made
from model_files.models import *

######################################################
# SETUP
######################################################
# Set up the Flask app

app = Flask(__name__)

cfg = load_config('app/config.yaml')

@app.before_request
def before_request():
    g.dbMain = dynamicDB.connect()


@app.teardown_request
def teardown_request(exception):
    dbM = getattr(g, 'db', None)
    if (dbM is not None) and (not dbM.is_closed()):
        dbM.close()

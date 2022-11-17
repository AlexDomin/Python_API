# config.py
import pathlib
import connexion
from flask import Flask, request, jsonify, make_response, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///widgets.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)

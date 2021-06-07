# import libarary Flask
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configuratis db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sentiment_latihan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
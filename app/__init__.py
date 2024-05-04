from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Assetmanagement@localhost/assetsmanagement'
db = SQLAlchemy(app)

from app import routes
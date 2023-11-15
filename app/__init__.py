from flask import Flask

# chapter 2: config
from config import Config

# chapter 3: database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#chapter 4: login system
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models

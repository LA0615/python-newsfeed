# from flask import Flask
# from app.routes import home, dashboard, api
# from app.db import init_db
# from app.utils import filters

# def create_app(test_config=None):
#   # set up app config
#   app = Flask(__name__, static_url_path='/')
#   app.url_map.strict_slashes = False
#   app.jinja_env.filters['format_url'] = filters.format_url
#   app.jinja_env.filters['format_date'] = filters.format_date
#   app.jinja_env.filters['format_plural'] = filters.format_plural 
#   app.register_blueprint(api)
#   app.config.from_mapping(
#     SECRET_KEY='super_secret_key'
#   )
#   # register routes 
#   app.register_blueprint(home)
#   app.register_blueprint(dashboard)
  
#   init_db(app)

#   return app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import home, dashboard, api
from app.db import init_db
from app.utils import filters

# Initialize SQLAlchemy with no database
db = SQLAlchemy()

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural'] = filters.format_plural 
  app.register_blueprint(api)
  app.config.from_mapping(
    SECRET_KEY='super_secret_key',
    SQLALCHEMY_DATABASE_URI=os.environ.get('JAWSDB_URL'),  # Use JAWSDB_URL from environment
    SQLALCHEMY_TRACK_MODIFICATIONS=False,  # Suppress a warning message
  )
  # register routes 
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  
  # Initialize the database with the app
  db.init_app(app)

  return app



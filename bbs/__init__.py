import flask
from bbs import views
from bbs.models import db

def create_app():
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    views.init_app(app)
    return app

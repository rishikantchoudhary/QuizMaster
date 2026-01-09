from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

from config import Config
app.config.from_object(Config)

import models
import routes

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return models.User.query.get(int(userid))

if __name__ == '__main__':
    app.run(debug=True)
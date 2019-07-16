import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from web.commons.helper.responses import response

app = Flask(__name__)
app.config.from_pyfile(os.path.join("..", "config/app.conf"), silent=False)
app.config['DEBUG'] = app.config.get("DEBUG")
app.config['ENV'] = app.config.get("ENVIRONMENT")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from web.auth.register.Register import register_module
from web.auth.login.Login import login_module
from web.property.Property import property_module

app.register_blueprint(register_module)
app.register_blueprint(login_module)
app.register_blueprint(property_module, url_prefix='/property')

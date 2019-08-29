import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from web.commons.helper.responses import response

app = Flask(__name__)
app.config.from_pyfile(os.path.join("..", "config/app.conf"), silent=False)
app.config['DEBUG'] = app.config.get("DEBUG")
app.config['ENV'] = app.config.get("ENVIRONMENT")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)


@app.route("/", methods=['GET'])
def hello():
    user = {'username': 'Gopi Krishna M'}
    return render_template('index.htm', title='Gopi',  user=user)


from web.auth.register.Register import register_module
from web.auth.login.Login import login_module
from web.property.Property import property_module

app.register_blueprint(register_module)
app.register_blueprint(login_module)
app.register_blueprint(property_module, url_prefix='/property')

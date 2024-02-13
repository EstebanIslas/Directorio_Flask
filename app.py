#Config de la aplicacion
from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/contacts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLAlchemy(app)

app.register_blueprint(contacts)
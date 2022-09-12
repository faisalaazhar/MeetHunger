from random import randint
from flask import *
from flask_mail import *
import bcrypt
import pymongo

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_TLS = False
MAIL_USE_SSL= True
MAIL_USERNAME = 'meet.hunger479@gmail.com'
MAIL_PASSWORD = 'aifshtenwrmksvkh'

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = db_client["user"]
db_x = db.user_info
db_blog = db.blog
db_contact = db.contact
db_money = db.donate_money
db_chef = db.chef

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

app.secret_key = "testing"

from app.routes import home
from app.routes import signup
from app.routes import login
from app.routes import logout
from app.routes import change_pass
from app.routes import verify
from app.routes import editprofile
from app.routes import aboutus
from app.routes import blog
from app.routes import requestChef
from app.routes import contactus
from app.routes import donate
from app.routes import chef
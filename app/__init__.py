from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://kmmukgsvzbjqkd:e9f3a080f742535d98cab8d3a3d20c371cbe536502b1878b14ee6e5fefb86eb0@ec2-34-193-232-231.compute-1.amazonaws.com:5432/dcdv4h4c7rqfsr"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']= './app/static/uploads'

db = SQLAlchemy(app)

### Flask-Login login manager
##login_manager = LoginManager()
##login_manager.init_app(app)
##login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views

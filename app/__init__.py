from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hhvyppyqidlyot:db72459834ff6efd52e9418ce825fa59942aa57329ced9a6ab6ab324cb0ce4a8@ec2-18-235-20-228.compute-1.amazonaws.com:5432/dd5sg5odja5546"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']= './app/static/uploads'

db = SQLAlchemy(app)

### Flask-Login login manager
##login_manager = LoginManager()
##login_manager.init_app(app)
##login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views

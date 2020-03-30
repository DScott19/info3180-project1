from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    firstname = TextField('First Name', validators=[DataRequired()])
    lastname = TextField('Last Name', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])
    location = TextField('Location', validators=[DataRequired()])
    gender = SelectField('Gender',choices = [('','Select Gender'),('Male','Male'),('Female','Female')],validators=[DataRequired()])
    biography=TextAreaField('Biography',validators=[DataRequired()])
    photo = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])


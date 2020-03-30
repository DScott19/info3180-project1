import datetime
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ProfileForm
from app.models import UserProfile
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
import os


def format_date_joined():
    date_joined = datetime.datetime.now()
    return date_joined.strftime("%B %d, %Y") 



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profiles')
def profiles():
    users = db.session.query(UserProfile).all() 
    ##image_list=get_uploaded_images();
    return render_template('profiles.html',users=users)

@app.route('/profile/<userid>')
def user_profile(userid):
    users=db.session.query(UserProfile).filter_by(userid=userid).all()
    return render_template('user_profile.html',users=users)


@app.route('/profile',methods=['GET','POST'])
def profile():
    form=ProfileForm()
    if request.method == "POST" and form.validate_on_submit():
        firstname=form.firstname.data
        lastname=form.lastname.data
        email=form.email.data
        location=form.location.data
        gender=form.gender.data
        biography=form.biography.data
        photo=form.photo.data
        filename=secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user=UserProfile(first_name=firstname,last_name=lastname,email=email,location=location,gender=gender,biography=biography,filename=filename,created_on=format_date_joined())
        db.session.add(user)
        db.session.commit()
        flash('Profile was successfully added','success')
        return redirect(url_for('profiles'))
    else:
        
        return render_template('profile.html',form=form)

        


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")


    
    



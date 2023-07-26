from flask import Flask, render_template, redirect, url_for
from forms import CourseForm, country_choices

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

courses_list = [{
    'firstname': 'John',
    'lastname': 'Doe',
    'email': 'john.doe@example.com',
    'message': 'Learn Python basics',
    'gender': True,
    'subject': ['repair', 'order', 'others'],
    'repair': True,
    'order': True,
    'others': False
    }]

@app.route('/', methods=('GET','POST'))
 
def index():
    form=CourseForm()
    form.country.choices = country_choices
   
    if form.validate_on_submit():
        # Check the honeypot field
        if form.email_confirm.data:
            # This is likely a spam submission, reject it
            return "Sorry, this form submission is not allowed."

        # Get the data from the form
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        country = form.country.data
        message = form.message.data
        gender = form.gender.data
        subjects = form.subject.data
        return redirect(url_for('success'))
    
# Process the form data for GET requests as well
     #form.process(data=courses_list[0])-->
    return render_template('index.html', form=form)
     
@app.route('/success')
def success():
    return "Form submitted successfully!" 

if __name__ == '__main__':
    app.run()
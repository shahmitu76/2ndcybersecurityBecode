from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectField, SelectMultipleField)
from wtforms.validators import InputRequired, Length, Email, DataRequired

# List of available country options for the SelectField
country_choices = [
    ('', 'Select a country'),
    ('USA', 'United States'),
    ('CAN', 'Canada'),
    ('UK', 'United Kingdom'),
    ('AUS', 'Australia'),
    # Add more countries as needed
]
class CourseForm(FlaskForm):
    firstname = StringField('FirstName', validators=[InputRequired(),
                                             Length(min=2, max=100)])
    lastname = StringField('LastName', validators=[InputRequired(),
                                             Length(min=2, max=100)])
    email = StringField('Email', validators=[InputRequired(),Email(message='Invalid email format' ),
                                             Length(min=10, max=100)])
    message = TextAreaField('Message',
                                validators=[InputRequired(),
                                              Length( max=100)])
    country = SelectField('Country', choices=country_choices, validators=[InputRequired()])
    gender = RadioField('Gender',
                       choices=['Female', 'Male'],
                       validators=[InputRequired()])
    subject = SelectMultipleField('Subject', choices=[
        ('repair', 'Repair'),
        ('order', 'Order'),
        ('others', 'Others')
    ], validators=[DataRequired()])
     #implementation of honeypot
    email_confirm = StringField('Email Confirm')
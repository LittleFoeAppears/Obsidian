from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email
from validators import validate_message_length

class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    country = SelectField('Country', choices=[('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK')], validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), validate_message_length])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    repair = BooleanField('Repair')
    order = BooleanField('Order')
    other = BooleanField('Other')
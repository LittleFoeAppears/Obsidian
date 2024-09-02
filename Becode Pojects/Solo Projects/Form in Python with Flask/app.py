from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email
from validators import validate_message_length

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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

@app.route('/')
def index():
    form = ContactForm()
    return render_template('form.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    form = ContactForm()
    if request.form.get('honeypot'):
        flash('Spam detected')
        return render_template('form.html', form=form)
    if form.validate_on_submit():
        # Process form data
        return redirect(url_for('thank_you'))
    else:
        flash('Error in form submission')
        return render_template('form.html', form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
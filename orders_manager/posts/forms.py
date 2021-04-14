from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    date = DateField('Date')
    order = TextAreaField('Order', validators=[DataRequired()])
    post_code = StringField('Post Code')
    submit = SubmitField('Post')

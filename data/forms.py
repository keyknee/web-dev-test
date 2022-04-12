from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateUserForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])

class CreateItemForm(FlaskForm):
    title = StringField('title',validators=[DataRequired()])

class ReviewItemForm(FlaskForm):
    pass
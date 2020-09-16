from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class NewBlogForm(FlaskForm):
    title = StringField('Title', validators=[
                        DataRequired(), Length(min=5, max=15)])
    author = StringField('Author', validators=[
        DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])

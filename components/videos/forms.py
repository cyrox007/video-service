from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired

from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


class VideoForm(FlaskForm):
    video_name = StringField("Name (Required field): ", validators=[DataRequired()])
    video_description = TextAreaField("Description: ", validators=[DataRequired()])
    video_cover = FileField(validators=[])
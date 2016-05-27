from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField

class MediaItemEntry(Form):
    name = StringField('Name')
    media = StringField('Media')
    score = IntegerField('Score')
    review = StringField('Review')
    dateviewed = DateTimeField('Date Viewed')
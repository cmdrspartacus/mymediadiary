from mediadiary import app
from flask import render_template
from .forms import MediaItemEntry
from flask import request
from .models import Item
from .database import db_session


@app.route('/')
def index():
    return render_template('landing.html', title='Chronoviz')


@app.route('/entry', methods=['GET', 'POST'])
def entry():
    form = MediaItemEntry(request.form)
    if request.method == 'POST' and form.is_submitted():
        # fields are assembled and submitted to the database.
        entrycomplete = [form.name.data, form.media.data, form.review.data]
        newitem = Item(form.name.data, form.media.data, form.review.data, form.score.data)
        db_session.add(newitem)
        db_session.commit()
        return render_template('entrycomplete.html', title='Entry Complete', entrycomplete=entrycomplete)
    return render_template('entry.html', form=form)

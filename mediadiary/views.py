from mediadiary import app
from flask import render_template, redirect, url_for
from .forms import MediaItemEntry


@app.route('/')
def index():
    return render_template('landing.html', title='Chronoviz')

@app.route('/entry', methods=['GET', 'POST'])
def entry():
    form = MediaItemEntry()
    if form.is_submitted():
        # fields are assembled and submitted to the database.

        return redirect(url_for('index'))
    return render_template('entry.html', form= form)
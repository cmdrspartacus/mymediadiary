from mediadiary import app
from flask import render_template


@app.route('/')
def template_test():
    return render_template('landing.html', title='Chronoviz')

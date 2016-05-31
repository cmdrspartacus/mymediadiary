from flask import Flask
from mediadiary.database import db_session

app = Flask(__name__)
app.debug = True
app.secret_key = 'onthewaterfront'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

import mediadiary.views
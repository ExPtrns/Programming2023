import datetime
from flask import (Flask)

app = Flask(__name__)

@app.route('/test')
def test():
    return 'test'
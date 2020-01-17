import os

from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    send_from_directory
)


load_dotenv()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    print(os.path.join(app.root_path, 'static'))
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

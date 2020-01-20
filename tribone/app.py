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


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


@app.route('/.well-known/pki-validation/18FA44ACD11780D440CDDF9880E184F1.txt')
def pki():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        '18FA44ACD11780D440CDDF9880E184F1.txt',
        mimetype='text/plain'
    )

import os

from flask import (
    Flask,
    render_template,
    send_from_directory
)
from flask_talisman import Talisman
from flask_seasurf import SeaSurf


app = Flask(__name__)  # skipcq: PYL-C0103
app.secret_key = os.getenv('SECRET_KEY', None)


Talisman(app)
SeaSurf(app)


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
        mimetype='image/vnd.microsoft.icon',
    )


@app.route('/resume.pdf')
def resume_pdf():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'resume.pdf',
        mimetype='application/pdf',
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)  # skipcq: BAN-B201

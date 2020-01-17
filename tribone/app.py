from dotenv import load_dotenv
from flask import Flask
from flask import render_template


load_dotenv()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

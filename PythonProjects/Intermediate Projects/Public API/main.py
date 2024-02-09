from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():

    welcome_phrase = 'Welcome to my first public API'
    return render_template('index.html', phrase=welcome_phrase, date=datetime.now())

if __name__ == '__main__':
    app.run()


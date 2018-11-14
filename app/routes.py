from flask import render_template
from app import app
from scrape import getWord
result = getWord()
word_send = result[0]
definitions_send = result[1:] # lol does this work?

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', word=word_send, definitions=definitions_send)

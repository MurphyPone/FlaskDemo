import sys
from flask import Flask, render_template, request, redirect, Response
from scrape import getWord
app = Flask(__name__)

result = getWord()
word_send = result[0]
definitions_send = result[1:] # lol does this work?
print("fetched the words")

@app.route("/")
def index():
    #return render_template("index.html", name="Joe")
    return render_template("index1.html", word=word_send, definitions=definitions_send, results=result)

@app.route('/receiver', methods = ['POST'])
def worker():
    # read json + reply
    data = request.get_json(force=True)
    return data

if __name__ == "__main__":
    #app.run()
	app.run("0.0.0.0", "8000")

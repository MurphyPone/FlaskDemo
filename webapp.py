from flask import Flask, render_template
from scrape import getWord
app = Flask(__name__)

result = getWord()
word_send = result[0]
definitions_send = result[1:] # lol does this work?
print("fetched the words")

@app.route("/")
def index():
    return render_template("index.html", word=word_send, definitions=definitions_send)

if __name__ == "__main__":
	app.run()

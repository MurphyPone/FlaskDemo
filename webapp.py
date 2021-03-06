import sys
from flask import Flask, render_template, request, redirect, Response
from flask_cors import CORS, cross_origin
from scrape import getWord
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

result = getWord() # get the word of the day from webscrape.py
word_send = result[0] # isolate the word to send to the server
definitions_send = result[1:] # isolate the definitions to send to the server
print("fetched the words")

# main page route
@app.route("/")
def index():
    return render_template("index1.html", word=word_send, definitions=definitions_send)

# post route #
@app.route('/receiver', methods = ['GET', 'POST'])
@cross_origin()
def worker():
    data = request.get_json(force=True) # grabbit
    result = process(data)  # process the data from JSON to string
    return result   # post the resulting string on the network???

@app.route('/test', methods = ['GET'])
def testPage():
    show = '<h1>' + word_send + '</h1>'
    for defn in definitions_send:
        show += '<p>' + defn + '</p>'
    return show

# HELPER METHOD
def process(data):
    result = ''
    for dict in data: # iterate over array [{'word': word}, {'definitions': [a,b,c ]}]
        for key, value in dict.items(): # iterate over {} {}
            if key == 'definitions':    # if it's another nested struct, then
                for defn in value:  # iterate over the [a, b, c]
                    result += str(defn) + '\n'
            else:
                result += str(value) + '\n'
    print(result)
    return result

# alias 'flask run' to 'python3 webapp.py'
if __name__ == "__main__":
    #app.run()
	app.run("0.0.0.0", "8000")

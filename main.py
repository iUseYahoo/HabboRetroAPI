import json
from flask import Flask, request, jsonify, render_template
from endpoints.hablit.hablit import hablit_search

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/get/search/', methods=['GET'])
def search_index():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        return json.dumps({'error:', 'You cannot use this method.'})

@app.route('/post/search/', methods=['POST'])
def search_post():
    if request.method == 'POST':
        username = request.form['username']

        # check for xss < > characters
        if "<" in username or ">" in username:
            return json.dumps({'error': 'Invalid characters in username.'})

        if username != "" or username != None:
            return hablit_search(username)
        else:
            return json.dumps({'error:', 'You must provide a username.'})
    else:
        return json.dumps({'error:', 'You cannot use this method, Please use POST instead of ' + request.method})

if __name__ == "__main__":
    app.run(debug=True)
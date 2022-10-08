import json
from flask import Flask, request, jsonify, render_template
from endpoints.hablit.hablit import hablit_search
from handler import handle

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
        retname = request.form['retname']
        username = request.form['username']

        if "<" in retname or ">" in retname:
            return json.dumps({'error': 'Invalid characters in retname.'})

        if "<" in username or ">" in username:
            return json.dumps({'error': 'Invalid characters in username.'})

        if retname != "" or username != "" or username != None:
            return handle(retname, username)
        else:
            return json.dumps({'error:', 'You must provide a valid retname and username.'})
    else:
        return json.dumps({'error:', 'You cannot use this method, Please use POST instead of ' + request.method})

if __name__ == "__main__":
    app.run(debug=True)
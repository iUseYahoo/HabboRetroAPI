import json
from endpoints.hablit.hablit import hablit_search

def handle(retname, username):
    if retname.lower() == "hablit":
        return hablit_search(username)
    else:
        return json.dumps({'error': 'Invalid retro name.'})
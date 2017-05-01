#!flask-ajax/bin/python
from flask import Flask, jsonify, request, session
app = Flask(__name__)
app.secret_key = 'joshsupersecret'

def safe_sess_json(session):
    finaldict = {}
    for thekey in ['shopInternet', 'filo', 'myAccount']:
        if thekey in session:
            finaldict[thekey] = session[thekey]
        else:
            finaldict[thekey] = 0
    return jsonify(finaldict)

@app.route('/', methods=['GET'])
def get_all_things():
        try:
            out = jsonify(shopInternet = session['shopInternet'],
                   filo = session['filo'],
                   myAccount = session['myAccount'])
        except KeyError:
            out = jsonify(message = 'No data yet')
        return out


@app.route('/event', methods=['POST'])
def increment_count():
    content = request.get_json()
    if 'eventName' in content:
        if not content['eventName'] in session:
            session[content['eventName']] = 1
        else:
            session[content['eventName']] += 1
    return safe_sess_json(session=session)



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=int("80"))


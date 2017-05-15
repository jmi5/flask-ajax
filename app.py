#!flask-ajax/bin/python

# Parse the results of submitting my-form.html and hit tip and return the results

from flask import Flask
from flask import request
from flask import render_template
import requests



# myip = '209.251.238.55'
# myua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# import json2html
# json2html.json2html.convert(json=resp.content)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    key = 's8v'
    ip = request.form['ip']
    useragent = request.form['useragent']
    # Parse out IP and UA and give some defaults
    # if ip == '':
    #     ip = '209.251.238.55'
    # if useragent == '':
    #     useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    resp = requests.get(url='https://tip.nimbus.tagular.com/lookup', params={'ua': useragent, 'ip': ip, 'key': key})
    return resp.content

if __name__ == '__main__':
    app.run(debug=True)
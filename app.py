#!flask-ajax/bin/python

# Parse the results of submitting my-form.html and hit tip and return the results

from flask import Flask
from flask import request
from flask import render_template
import requests

# import urllib
# urllib.unquote_plus("[{&#34;geo&#34;:{&#34;asn&#34;:&#34;0&#34;,&#34;asn-name&#34;:&#34;?&#34;,&#34;company-name&#34;:&#34;?&#34;,&#34;country-name&#34;:&#34;reserved/private&#34;,&#34;domain-name&#34;:&#34;?&#34;,&#34;edge-area-codes&#34;:&#34;?&#34;,&#34;edge-city&#34;:&#34;reserved&#34;,&#34;edge-conn-speed&#34;:&#34;broadband&#34;,&#34;edge-country&#34;:&#34;***&#34;,&#34;edge-gmt-offset&#34;:&#34;+9999&#34;,&#34;edge-in-dst&#34;:&#34;n&#34;,&#34;edge-latitude&#34;:&#34;0&#34;,&#34;edge-longitude&#34;:&#34;0&#34;,&#34;edge-metro-code&#34;:&#34;-1&#34;,&#34;edge-postal-code&#34;:&#34;0&#34;,&#34;edge-region&#34;:&#34;***&#34;,&#34;edge-two-letter-country&#34;:&#34;**&#34;,&#34;end_ip&#34;:&#34;127.0.0.37&#34;,&#34;homebiz-type&#34;:&#34;?&#34;,&#34;is-an-isp&#34;:&#34;no&#34;,&#34;isp-name&#34;:&#34;?&#34;,&#34;metro-name&#34;:&#34;not metroized&#34;,&#34;metro-regions&#34;:&#34;?&#34;,&#34;naics-code&#34;:&#34;0&#34;,&#34;organization-name&#34;:&#34;internet assigned numbers authority&#34;,&#34;primary-lang&#34;:&#34;?&#34;,&#34;proxy-description&#34;:&#34;?&#34;,&#34;proxy-type&#34;:&#34;?&#34;,&#34;secondary-lang&#34;:&#34;?&#34;,&#34;start_ip&#34;:&#34;127.0.0.0&#34;},&#34;ua&#34;:{&#34;_matched&#34;:&#34;Mozilla/5.0 (Macintosh; AppleWebKit (KHTML, like Gecko) Chrome Safari&#34;,&#34;_unmatched&#34;:&#34;&#34;,&#34;browserName&#34;:&#34;Chrome&#34;,&#34;browserRenderingEngine&#34;:&#34;WebKit&#34;,&#34;browserVersion&#34;:&#34;58.0.3029.110&#34;,&#34;isApp&#34;:0,&#34;isBrowser&#34;:1,&#34;isChecker&#34;:0,&#34;isDownloader&#34;:0,&#34;isEReader&#34;:0,&#34;isFeedReader&#34;:0,&#34;isFilter&#34;:0,&#34;isGamesConsole&#34;:0,&#34;isMediaPlayer&#34;:0,&#34;isMobilePhone&#34;:0,&#34;isRobot&#34;:0,&#34;isSetTopBox&#34;:0,&#34;isSpam&#34;:0,&#34;isTV&#34;:0,&#34;isTablet&#34;:0,&#34;manufacturer&#34;:&#34;Apple&#34;,&#34;mobileDevice&#34;:0,&#34;model&#34;:&#34;Chrome - OS X&#34;,&#34;ms&#34;:0,&#34;osAndroid&#34;:0,&#34;osBada&#34;:0,&#34;osName&#34;:&#34;OS X&#34;,&#34;osRim&#34;:0,&#34;osSymbian&#34;:0,&#34;osVersion&#34;:&#34;10_11_1&#34;,&#34;osWebOs&#34;:0,&#34;osWindowsMobile&#34;:0,&#34;osWindowsPhone&#34;:0,&#34;osWindowsRt&#34;:0,&#34;osiOs&#34;:0,&#34;primaryHardwareType&#34;:&#34;Desktop&#34;,&#34;touchScreen&#34;:0,&#34;vendor&#34;:&#34;Google&#34;},&#34;time_ms&#34;:0.878362,&#34;geo_time_ms&#34;:0.526173,&#34;ua_time_ms&#34;:0.876028,&#34;original_ip&#34;:&#34;127.0.0.1&#34;,&#34;original_ua&#34;:&#34;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36&#34;}]")

# import urllib2
# urllib2.unquote('{&#34;geo&#34;:{&#34;asn').decode('utf8')


# myip = '209.251.238.55'
# myua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# import json2html
# json2html.json2html.convert(json=resp.content)


app = Flask(__name__, static_folder='static')
# app = Flask(__name__, template_folder='', static_folder='')

@app.route('/', methods=['GET'])
def my_form():
    # return render_template("my-form.html")
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    key = 's8v'
    ip = request.form['ip']
    useragent = request.form['useragent']
    # Parse out IP and UA and give some defaults
    if ip == '':
        # Edit: see http://esd.io/blog/flask-apps-heroku-real-ip-spoofing.html
        # ip = request.remote_addr
        if not request.headers.getlist("X-Forwarded-For"):
            ip = request.remote_addr
        else:
            ip = request.headers.getlist("X-Forwarded-For")[0]
    if useragent == '':
        useragent = request.user_agent
    resp = requests.get(url='https://tip.nimbus.tagular.com/lookup', params={'ua': useragent, 'ip': ip, 'key': key})
    # return resp.content
    return render_template('results.html', result=str(resp.text))

if __name__ == '__main__':
    app.run(debug=True)
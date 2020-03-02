from flask import request
import json
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def homepage():
    ip_addr = get_my_ip()
    location = get_loc(ip_addr)
    weather = get_weather(location)
    return render_template('index.html', ip_addr = ip_addr['ip'], location = location,weather = weather)

def get_my_ip():
      return ({'ip': request.remote_addr})

def get_loc(ip_addr):
    r = requests.get(
        'http://ipinfo.io/{}/loc?token=616e00cc38bf93'.format(ip_addr))
    r = list(map(float, r.text.split(',')))
    return r

def get_weather(location):
    apikey = '3fdyEZlSmoXgwSSrnNyinm8Pg9WAy4eMtoTElg5Op8I'
    r = requests.get(
        'https://weather.ls.hereapi.com/weather/1.0/report.json?product=observation&latitude={}&longitude={}&oneobservation=true&apiKey={}'.format(location[0],location[1],apikey))
    return json.loads(r.text)


if __name__ == "__main__":
    app.run()

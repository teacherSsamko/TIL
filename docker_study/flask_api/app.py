from flask import Flask
import requests


app = Flask('api_test')


@app.route('/')
def hello():
    return 'hello'


@app.route('/upscaling')
def check_upscaling():
    url = 'https://host/check_upscaling'
    res = requests.get(url)
    return f'{res.status_code} - {res.text}'


@app.route('/upload')
def check_upload():
    url = 'https://host/upload'
    data = 'file here'
    res = requests.post(url, data=data)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

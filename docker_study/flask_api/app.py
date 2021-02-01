from flask import Flask
import requests


app = Flask('api_test')


@app.route('/')
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# save this as app.py
from flask import Flask, request

app = Flask(__name__,
    static_url_path='',
    static_folder='static'
)

@app.route("/hola")
def hello():
    return request.base_url
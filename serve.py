import requests
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def index_page():
    return app.send_static_file("index.html")


@app.route("/structuring", methods=["POST"])
def structuring():
    rsp = requests.post("http://101.200.120.155:8705/structuring", data={"text": request.form["text"]})
    return rsp.text


if __name__ == "__main__":
    app.run(host="localhost", port=28810)

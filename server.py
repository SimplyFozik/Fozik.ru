from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")
@app.route("/exit")
def exitServer():
    return exit()
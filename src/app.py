from flask import Flask, request, redirect, render_template
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.value = 0
    return redirect("/")

@app.route("/set", methods=["POST"])
def set_value():
    new_value = int(request.form["value"])
    cnt.set_value(new_value)
    return redirect("/")

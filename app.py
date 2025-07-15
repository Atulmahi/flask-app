from flask import Flask, render_demo

app = Flask(__name__)

@app.route('/')
def index():
    return render_demo("demo.html")

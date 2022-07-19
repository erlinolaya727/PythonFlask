from flask import Flask, render_templeate

app = Flask(__name__)

@app.route('/')
def index():
    return render_templeate('index.html')
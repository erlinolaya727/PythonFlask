from env import app
from flask import Flask, render_template

if __name__ == '__main__':
    app.run(debug = True)
    
@app.route('/')
def home_page():
    return render_template('controlAdmin.html')
#!/usr/bin/python3
"""
    Sript that starts a Flask web application
 """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
        function main page
    """
    return render_template('index.html')


@app.route('/GovTech', strict_slashes=False)
def hbnb():
    """
        function to return GovTech
    """
    return render_template('base.html')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5001)
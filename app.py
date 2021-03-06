"""
    Windows: python app.py
    MacOS: python3 app.py
"""

import os
from datetime import datetime, timedelta
from flask import Flask, redirect, render_template, request, flash, session, url_for, send_file
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
app.config['SECRET_KEY'] = ""
app.config['TEMPLATES_AUTO_RELOAD'] = True

mysql = MySQL(app)


@app.route("/")
def home():
    """Renders the HTML for the main page of the website.

    Returns:
        Str: The rendered HTML for the main page.
    """
    return render_template('index.j2')

@app.route("/about")
def about():
    """Renders the HTML for the "about me" page of the website.

    Returns:
        Str: The rendered HTML for the about page.
    """
    return render_template('about.j2')

@app.route("/resume")
def download():
    """Downloads resume from the website.

    Returns:
        Download: PDF of resume.
    """
    path = "static/Kevin-Kraatz-Resume.pdf"
    return send_file(path, as_attachment=True)




if __name__ == "__main__":

    app.run(debug=True)

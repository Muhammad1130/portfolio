from flask import Flask, render_template, request, redirect
import os 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

if __name__ == '__main__':
    app.run(debug=True)
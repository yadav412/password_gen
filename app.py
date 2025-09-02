#random password generator
from flask import Flask, render_template, request
import random
import string
import secrets as secret

app= Flask(__name__)

sp= ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/"]

def generate_password(length):
    password= ""
    for i in range(length):
        password = password + secret.choice (string.ascii_letters + string.digits + random.choice(sp))
    return password

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)
        return render_template('index.html', password=password)
    return render_template('index.html', password=None)

if __name__ == '__main__':
    app.run(debug=True)
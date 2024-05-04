from flask import Flask, render_template, request
from password_genrator import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    password_length = int(request.form['length'])
    include_uppercase = 'uppercase' in request.form
    include_lowercase = 'lowercase' in request.form
    include_digits = 'digits' in request.form
    include_special = 'special' in request.form
    password = generate_password(password_length, include_uppercase, include_lowercase, include_digits, include_special)

    return password

if __name__ == '__main__':
    app.run()

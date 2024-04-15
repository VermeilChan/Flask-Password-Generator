from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    characters = ''
    if include_uppercase:
        characters += ascii_uppercase
    if include_lowercase:
        characters += ascii_lowercase
    if include_digits:
        characters += digits
    if include_special:
        characters += punctuation
    generated_password = ''.join(choice(characters) for _ in range(length))
    return generated_password

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

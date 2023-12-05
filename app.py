from flask import Flask, render_template, request
import random


app = Flask(__name__, static_url_path='/static')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$*^&%/(),;?0123456789'

def generate_password(length):
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_passwords():
    number = int(request.form.get('number'))
    length = int(request.form.get('length'))
    passwords = [generate_password(length) for _ in range(number)]
    return render_template('passwords.html', passwords=passwords)

if __name__ == '__main__':
    app.run(debug=True)
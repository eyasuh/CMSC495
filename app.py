from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/registration')
def register():
    return render_template('registration.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

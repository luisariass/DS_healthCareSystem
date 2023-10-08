from flask import Flask, render_template
from flask import Blueprint, render_template


app = Flask(__name__)
bp = Blueprint('main', __name__)

@app.route('/')
def home():
    return render_template ('home.html')


@app.route('/login')
def login():
    return render_template ('login.html')


@app.route('/agendamiento')
def agenda():
    return render_template ('agendamiento.html')



if __name__ == '__main__':
    app.run(debug=True)
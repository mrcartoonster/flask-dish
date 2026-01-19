from flask import Flask
from mimesis import Generic


g = Generic()

app = Flask(__name__)


@app.route('/')
def home():
    return f'Hello, Flask! The dish you should try is {g.food.dish()}. Yummy!'
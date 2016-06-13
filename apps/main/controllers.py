from flask import Flask, render_template
from flask import Blueprint

# Modular app
main = Blueprint('main', __name__)


@main.route('/')
def hello_world():
    return render_template("main/index.html")

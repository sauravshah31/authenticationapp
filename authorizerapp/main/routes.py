from flask import (
    Blueprint,
    current_app,
    render_template
)


main = Blueprint('main',__name__)

@main.route("/")
def homepage():
    return render_template('index.html'),200
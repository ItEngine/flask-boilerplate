from flask import Blueprint, Flask, render_template
from flask.views import View


# Modular app
main = Blueprint('main', __name__)


class IndexView(View):
    """
    Index main view
    """
    def dispatch_request(self):
        # templates located in templates directory by default
        return render_template("main/index.html")


main.add_url_rule('/', view_func=IndexView.as_view('index'))

from flask import render_template
from flask.views import View


class IndexView(View):
    """
    Index main view
    """
    def dispatch_request(self):
        # templates located in templates directory by default
        return render_template("main/index.html")

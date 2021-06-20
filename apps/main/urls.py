from flask import Blueprint
from apps.main import controllers


blueprint = Blueprint('main', __name__)
blueprint.add_url_rule(
    '/', view_func=controllers.IndexView.as_view('index')
)

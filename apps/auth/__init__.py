from flask import Blueprint, current_app
from apps.auth.api import GetUsers


blueprint = Blueprint('auth', __name__)
current_app.api.add_resource(GetUsers, '/api/getusers')

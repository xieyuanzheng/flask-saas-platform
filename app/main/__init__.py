from flask import Blueprint

main = Blueprint('main', __name__, template_folder="app/templates", static_folder="app/static")

from . import views, forms, errors

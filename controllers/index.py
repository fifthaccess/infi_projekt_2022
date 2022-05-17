from flask.templating import render_template
from flask import Blueprint


index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route("/")
def index():

    # , form = addItemFormObject, items = items)
    return render_template("index.html", headline="Übersicht")

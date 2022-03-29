from operator import index
from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from model.models import db,Kuenstler

index_blueprint = Blueprint('index_blueprint',__name__)


@index_blueprint.route("/")
def index():

    return render_template("index.html", headline="Übersicht")#, form = addItemFormObject, items = items)
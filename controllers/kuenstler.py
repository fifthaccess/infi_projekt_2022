from ast import Del
from operator import index
from pyexpat import model
import string
from click import edit
from flask import Flask, redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import sqlalchemy.orm
from model.models import Kuenstler, db


kuenstler_blueprint = Blueprint('kuenstler_blueprint',__name__)


@kuenstler_blueprint.route("/kuenstler")
def kuenstler_view():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    kuenstler = session.query(Kuenstler).order_by(Kuenstler.KuenstlerId).all() 
    
    return render_template("manager/viewmanagers.html", managers = kuenstler, headline = "Kuenstler")

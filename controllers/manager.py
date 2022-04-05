from operator import index
from pyexpat import model
from flask import Flask, redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import sqlalchemy.orm
from model.models import db
from forms.Manager import ManagerForm
from model.models import Manager

manager_blueprint = Blueprint('manager_blueprint',__name__)


@manager_blueprint.route("/managers")
def manager_view():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    managers = session.query(Manager).order_by(Manager.ManagerId).all() 
    
    return render_template("manager/viewmanagers.html", managers = managers, headline = "Managers")

@manager_blueprint.route('/managers/add', methods=["Get", "Post"])
def manager_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    add_manager_form = ManagerForm()

    if request.method == 'Post':

        if add_manager_form.validate_on_submit():
            new_manager =  ManagerForm()

            print(add_manager_form.Nachname)
            #new_manager.ManagerId = add_manager_form.ManagerID.data
            new_manager.Vorname = add_manager_form.Vorname.data
            new_manager.Nachname = add_manager_form.Nachname.data
            new_manager.Firma = add_manager_form.Firma.data
            new_manager.Kuenstler_anzahl = add_manager_form.Kuenstler_anzahl.data 

            db.session.add(new_manager)
            db.session.commit()

            return redirect("/managers")

        else:
            return render_template("manager/addmanager.html", managers = add_manager_form, headline = "Add Managers")
    else:
        return render_template("manager/addmanager.html", managers = add_manager_form, headline = "Add Managers", form = add_manager_form)

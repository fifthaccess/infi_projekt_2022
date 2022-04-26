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
from model.models import db
from forms.Manager import ManagerForm , DeleteManagerFrom, editManagerForm
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
    managers = session.query(Manager).order_by(Manager.ManagerId).all() 
    if request.method == 'POST':
        print("f")
        if add_manager_form.validate_on_submit():
            new_manager =  Manager()

            print(add_manager_form.Nachname.data)
            #new_manager.ManagerId = add_manager_form.ManagerID.data
            new_manager.Vorname = add_manager_form.Vorname.data
            new_manager.Nachname = add_manager_form.Nachname.data
            new_manager.Firma = add_manager_form.Firma.data
            new_manager.Kuenstler_anzahl = add_manager_form.Kuenstler_anzahl.data 

            db.session.add(new_manager)
            db.session.commit()

            return redirect("/managers")

        else:
            return render_template("manager/addmanager.html", headline = "Add Managers", form = add_manager_form, managers = managers)
        
    else:
        return render_template("manager/addmanager.html", headline = "Add Managers", form = add_manager_form, managers = managers)                   

@manager_blueprint.route('/managers/delete', methods=["Get", "Post"])
def manager_delete():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    managers = session.query(Manager).order_by(Manager.ManagerId).all() 
    del_form = DeleteManagerFrom()
    
    if request.method == 'POST':
        print("f")
        if del_form.validate_on_submit():
            delete_id_string = del_form.CheckedCheckboxes.data
            delete_id_list = list(delete_id_string.split(","))

            print(del_form.CheckedCheckboxes.data)
            for i in delete_id_list:
                print("deleting now data with id " + i)
                itemToDelete = db.session.query(Manager).filter(Manager.ManagerId == i)
                itemToDelete.delete()
                db.session.commit()
                print("deleted data with id " + i)

            managers = session.query(Manager).order_by(Manager.ManagerId).all() 
            return render_template("manager/viewmanagers.html", managers = managers, headline = "Managers", form = del_form )
        else:
            print("invalide Form")
            return render_template("manager/deleteManager.html", managers = managers, headline = "Delete Managers", form = del_form )
        
    else:
        return render_template("manager/deleteManager.html", managers = managers, headline = "Delete Managers", form = del_form )

@manager_blueprint.route('/managers/edit', methods=["Get", "Post"])
def manager_edit():
    edit_manager_id = request.args["itemid"]
    edit_manager_form = editManagerForm()
    item_to_edit = db.session.query(Manager).filter(Manager.ManagerId == edit_manager_id).first()
    if request.method == 'POST':
        print("Post")
        if edit_manager_form.validate_on_submit():
            print("is validate")
            

            item_to_edit.ManagerId = edit_manager_form.ManagerID.data 
            item_to_edit.Vorname = edit_manager_form.Vorname.data 
            item_to_edit.Nachname = edit_manager_form.Nachname.data 
            item_to_edit.Firma = edit_manager_form.Firma.data 
            item_to_edit.Kuenstler_anzahl = edit_manager_form.Kuenstler_anzahl.data 
            db.session.commit()
            return redirect("/managers")
    else:
        
        edit_manager_form.ManagerID.data = item_to_edit.ManagerId
        edit_manager_form.Vorname.data = item_to_edit.Vorname
        edit_manager_form.Nachname.data = item_to_edit.Nachname
        edit_manager_form.Firma.data = item_to_edit.Firma
        edit_manager_form.Kuenstler_anzahl.data = item_to_edit.Kuenstler_anzahl
        return render_template("manager/editmanager.html", headline = "Edit Managers", form = edit_manager_form)


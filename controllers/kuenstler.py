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
from forms.Kuenstler import KuenstlerForm, DeleteKuenstlerForm
from model.models import Kuenstler, db


kuenstler_blueprint = Blueprint('kuenstler_blueprint',__name__)


@kuenstler_blueprint.route("/kuenstler")
def kuenstler_view():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    kuenstler = session.query(Kuenstler).order_by(Kuenstler.KuenstlerId).all() 
    
    return render_template("kuenstler/viewKuenstler.html", kuenstlers = kuenstler, headline = "Kuenstler") # kuenstlers wird nur beutzt wegen dem identischen pural wie singular von kuenstler 


@kuenstler_blueprint.route('/kuenstler/add', methods=["Get", "Post"])
def kuenstler_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session

    add_kuenstler_form = KuenstlerForm()
    kuenstler = session.query(Kuenstler).order_by(Kuenstler.KuenstlerId).all()  
    
    if request.method == 'POST':
        print("f")
        if add_kuenstler_form.validate_on_submit():
            new_kuenstler =  Kuenstler()

            print("data is valid")
            #new_manager.ManagerId = add_manager_form.ManagerID.data

            new_kuenstler.Vorname = add_kuenstler_form.Vorname.data
            new_kuenstler.Nachname = add_kuenstler_form.Nachname.data
            new_kuenstler.ManagerId = add_kuenstler_form.ManagerID.data
            new_kuenstler.Herkunftsland = add_kuenstler_form.Herkunftsland.data 
            new_kuenstler.Gehalt = add_kuenstler_form.Gehalt.data
            db.session.add(new_kuenstler)
            db.session.commit()

            return redirect("/kuenstler")

        else:
            return render_template("kuenstler/addkuenstler.html", headline = "Add Künstler", form = add_kuenstler_form, kuenstlers = kuenstler)
        
    else:
        return render_template("kuenstler/addkuenstler.html", headline = "Add Künstler", form = add_kuenstler_form, kuenstlers = kuenstler)                   


@kuenstler_blueprint.route('/kuenstler/delete', methods=["Get", "Post"])
def manager_delete():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    kuenstler = session.query(Kuenstler).order_by(Kuenstler.KuenstlerId).all() 

    del_form = DeleteKuenstlerForm()
    
    if request.method == 'POST':
        print("f")
        if del_form.validate_on_submit():
            delete_id_string = del_form.CheckedCheckboxes.data
            delete_id_list = list(delete_id_string.split(","))

            print(del_form.CheckedCheckboxes.data)
            for i in delete_id_list:
                print("deleting now data with id " + i)
                itemToDelete = db.session.query(Kuenstler).filter(Kuenstler.KuenstlerId == i)
                itemToDelete.delete()
                db.session.commit()
                print("deleted data with id " + i)

            kuenstler = session.query(Kuenstler).order_by(Kuenstler.KuenstlerId).all() 
            return render_template("manager/viewmanagers.html", kuenstlers = kuenstler, headline = "Künstler", form = del_form )
        else:
            print("invalide Form")
            return render_template("manager/deletemanager.html", kuenstlers = kuenstler, headline = "Delete Künstler", form = del_form )
        
    else:
        return render_template("manager/deletemanager.html", kuenstlers = kuenstler, headline = "Delete Künstler", form = del_form )
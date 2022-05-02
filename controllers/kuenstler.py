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
from forms.Kuenstler import KuenstlerForm, DeleteKuenstlerForm, editKuenstlerForm
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
            return render_template("kuenstler/viewkuenstler.html", kuenstlers = kuenstler, headline = "Künstler", form = del_form )
        else:
            print("invalide Form")
            return render_template("kuenstler/deletekuenstler.html", kuenstlers = kuenstler, headline = "Delete Künstler", form = del_form )
        
    else:
        return render_template("kuenstler/deletekuenstler.html", kuenstlers = kuenstler, headline = "Delete Künstler", form = del_form )

@kuenstler_blueprint.route('/kuenstler/edit', methods=["Get", "Post"])
def kuenstler_edit():
    edit_kuenstler_id = request.args["itemid"]
    edit_kuenstler_form = editKuenstlerForm()

    item_to_edit = db.session.query(Kuenstler).filter(Kuenstler.KuenstlerId == edit_kuenstler_id).first()

    if request.method == 'POST':
        print("Post")
        if edit_kuenstler_form.validate_on_submit():
            print("is validate")
            

            item_to_edit.kuenstlerId = edit_kuenstler_form.KuenstlerId.data 
            item_to_edit.ManagerId = edit_kuenstler_form.ManagerID.data 
            item_to_edit.Vorname = edit_kuenstler_form.Vorname.data 
            item_to_edit.Nachname = edit_kuenstler_form.Nachname.data 
            item_to_edit.Herkunftsland = edit_kuenstler_form.Herkunftsland.data 
            item_to_edit.Gehalt = edit_kuenstler_form.Gehalt.data 
            db.session.commit()
            return redirect("/kuenstler")
    else:
        
        edit_kuenstler_form.KuenstlerId.data = item_to_edit.KuenstlerId
        edit_kuenstler_form.ManagerID.data = item_to_edit.ManagerId
        edit_kuenstler_form.Vorname.data = item_to_edit.Vorname
        edit_kuenstler_form.Nachname.data = item_to_edit.Nachname
        edit_kuenstler_form.Herkunftsland.data  = item_to_edit.Herkunftsland
        edit_kuenstler_form.Gehalt.data  = item_to_edit.Gehalt
        return render_template("kuenstler/editkuenstler.html", headline = "Edit Kuenstler", form = edit_kuenstler_form)
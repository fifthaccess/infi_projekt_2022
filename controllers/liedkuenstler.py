from unittest import expectedFailure
from flask import redirect, request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import sqlalchemy.orm
from forms.lied_kuenstler import LiedKuenstlerForm ,deleteLiedKuenstlerForm
from model.models import Kuenstler, db, LiedKuenstler 


lied_kuenstler_blueprint = Blueprint('lied_kuenstler_blueprint', __name__)


@lied_kuenstler_blueprint.route("/lieder")
def Lieder_view():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    lied = session.query(LiedKuenstler).order_by(LiedKuenstler.Id).all()

    return render_template("lieder/viewlieder.html", lieder=lied, headline="Lieder")


@lied_kuenstler_blueprint.route('/lied_kuenstler/add', methods=["Get", "Post"])
def Lied_kuenstler_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    item_to_attach_id = request.args["itemid"]
    add_lied_kuenstler_form = LiedKuenstlerForm()
    connected_kuenstler = session.query(LiedKuenstler).filter(LiedKuenstler.LiedId == item_to_attach_id).all()
    all_kuenstler = session.query(Kuenstler).order_by(Kuenstler.KuenstlerId).all()
    kuenstler = []
    try: 
        for n in all_kuenstler:
            for i in connected_kuenstler:
                if n == i:
                kuenstler.append(session.query(Kuenstler).filter(not(Kuenstler.KuenstlerId == i.KuenstlerId)).first())

    except AttributeError:
        kuenstler = session.query(Kuenstler).order_by(Kuenstler.KuenstlerId).all()
    if request.method == 'POST':
        print("f")
        if add_lied_kuenstler_form.validate_on_submit():
            print(add_lied_kuenstler_form.CheckedCheckboxes.data)
            kuenstler_ids_to_add = add_lied_kuenstler_form.CheckedCheckboxes.data

            new_Lied_Kuenstler = LiedKuenstler()

            print("data is valid")
            # new_manager.ManagerId = add_manager_form.ManagerID.data
            for i in kuenstler_ids_to_add:
                new_Lied_Kuenstler.KuenstlerId = int(i)
                new_Lied_Kuenstler.LiedId = item_to_attach_id
                db.session.add(new_Lied_Kuenstler)

            db.session.commit()

            return redirect("/lieder/edit?itemid=" + item_to_attach_id)

        else:
            return render_template(
            "liedkuenstler/liedkuenstleradd.html",
            headline="Add Lieder",
            kuenstlers = kuenstler,
            form = add_lied_kuenstler_form)

    else:
        return render_template(
            "liedkuenstler/liedkuenstleradd.html",
            headline="Add Lieder",
            kuenstlers = kuenstler,
            form = add_lied_kuenstler_form)


@lied_kuenstler_blueprint.route('/lied_kuenstler/delete', methods=["Get", "Post"])
def lied_kuenstler_delete():

    session: sqlalchemy.orm.scoping.scoped_session = db.session
    item_to_attach_id = request.args["itemid"]
    connected_kuenstler = session.query(LiedKuenstler).filter(LiedKuenstler.LiedId == item_to_attach_id).all()
    kuenstler = []
    try: 
        for i in connected_kuenstler:
            kuenstler.append(session.query(Kuenstler).filter(Kuenstler.KuenstlerId == i.KuenstlerId).first())
    except AttributeError:
        kuenstler = session.query(Kuenstler).order_by(Kuenstler.KuenstlerId).all()

    del_form = deleteLiedKuenstlerForm()

    if request.method == 'POST':
        print("f")
        if del_form.validate_on_submit():
            delete_id_string = del_form.CheckedCheckboxes.data
            delete_id_list = list(delete_id_string.split(","))

            print(del_form.CheckedCheckboxes.data)
            for i in delete_id_list:
                print("deleting now data with id " + i)
                itemToDelete = db.session.query(Lied).filter(Lied.LiedId == i)
                itemToDelete.delete()
                db.session.commit()
                print("deleted data with id " + i)

            lied = session.query(Lied).order_by(Lied.LiedId).all()
            return render_template(
                "lieder/viewlieder.html",
                lieder=lied,
                headline="Lieder",
                form=del_form)
        else:
            print("invalide Form")
            return render_template(
                "lieder/deletelieder.html",
                lieder=lied,
                headline="Delete Lieder",
                form=del_form)

    else:
        return render_template(
            "liedkuenstler/liedkuenstlerdelete.html",
            headline="Add Lieder",
            kuenstlers = kuenstler,
            form = del_form)


@lied_kuenstler_blueprint.route('/lied_kuenstler/edit', methods=["Get", "Post"])
def lied_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    edit_lied_id = request.args["itemid"]
    edit_lied_form = EditLiedForm()

    item_to_edit = db.session.query(Lied).filter(
        Lied.LiedId == edit_lied_id).first()

    item_to_edit_details_query: sqlalchemy.orm.query.Query = session.query(LiedKuenstler)

    item_to_edit_details = item_to_edit_details_query.\
        filter(LiedKuenstler.LiedId == edit_lied_id).\
        order_by(LiedKuenstler.KuenstlerId).all()

    if request.method == 'POST':
        print("Post")
        if edit_lied_form.validate_on_submit():
            print("is validate")

            item_to_edit.LiedId = edit_lied_form.LiedId.data
            item_to_edit.Kuenstleranzahl = edit_lied_form.Kuenstleranzahl.data
            item_to_edit.Liedname = edit_lied_form.Liedname.data
            item_to_edit.Erscheinungsdatum = edit_lied_form.Erscheinungsdatum.data
            db.session.commit()
            return redirect("/lieder")
    else:

        edit_lied_form.LiedId.data = item_to_edit.LiedId
        edit_lied_form.Kuenstleranzahl.data = item_to_edit.Kuenstleranzahl
        edit_lied_form.Liedname.data = item_to_edit.Liedname
        edit_lied_form.Erscheinungsdatum.data = item_to_edit.Erscheinungsdatum
        return render_template(
            "lieder/editlieder.html",
            headline="Edit Lieder",
            lieder=item_to_edit_details,
            form=edit_lied_form)

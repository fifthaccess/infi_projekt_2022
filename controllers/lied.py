from flask import redirect, request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import sqlalchemy.orm
from forms.lied import DeleteLiederForm, EditLiedForm, LiedForm
from model.models import Lied, db, LiedKuenstler


lied_blueprint = Blueprint('lied_blueprint', __name__)


@lied_blueprint.route("/lieder")
def Lieder_view():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    lied = session.query(Lied).order_by(Lied.LiedId).all()

    return render_template("lieder/viewlieder.html", lieder=lied, headline="Lieder")


@lied_blueprint.route('/lieder/add', methods=["Get", "Post"])
def Lieder_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    add_lied_form = LiedForm()
    lied = session.query(Lied).order_by(Lied.LiedId).all()

    if request.method == 'POST':
        print("f")
        if add_lied_form.validate_on_submit():
            new_Lied = Lied()

            print("data is valid")
            # new_manager.ManagerId = add_manager_form.ManagerID.data

            new_Lied.Kuenstleranzahl = add_lied_form.Kuenstleranzahl.data
            new_Lied.Liedname = add_lied_form.Liedname.data
            new_Lied.Erscheinungsdatum = add_lied_form.Erscheinungsdatum.data
            db.session.add(new_Lied)
            db.session.commit()

            return redirect("/lieder")

        else:
            return render_template(
                "lieder/addlieder.html",
                headline="Add Lieder",
                form=add_lied_form,
                lieder=lied)

    else:
        return render_template(
            "lieder/addlieder.html",
            headline="Add Lieder",
            form=add_lied_form,
            lieder=lied)


@lied_blueprint.route('/lieder/delete', methods=["Get", "Post"])
def lied_delete():

    session: sqlalchemy.orm.scoping.scoped_session = db.session
    lied = session.query(Lied).order_by(Lied.LiedId).all()

    del_form = DeleteLiederForm()

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
            "lieder/deletelieder.html",
            lieder=lied,
            headline="Delete Lieder",
            form=del_form)


@lied_blueprint.route('/lieder/edit', methods=["Get", "Post"])
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

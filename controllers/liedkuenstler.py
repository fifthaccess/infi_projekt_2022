from flask import redirect, request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import sqlalchemy.orm
from forms.lied_kuenstler import LiedKuenstlerForm, deleteLiedKuenstlerForm
from model.models import Kuenstler, db, LiedKuenstler


lied_kuenstler_blueprint = Blueprint('lied_kuenstler_blueprint', __name__)


@lied_kuenstler_blueprint.route("/lieder")
def Lieder_view():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    lied = session.query(LiedKuenstler).order_by(LiedKuenstler.Id).all()

    return render_template("lieder/viewlieder.html", lieder=lied, headline="Lieder")


@lied_kuenstler_blueprint.route('/lied_kuenstler/add', methods=["Get", "Post"])
def Liedkuenstler_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    item_to_attach_id = request.args["itemid"]
    add_lied_kuenstler_form = LiedKuenstlerForm()
    connected_kuenstler = session.query(LiedKuenstler).filter(
        LiedKuenstler.LiedId == item_to_attach_id).all()
    all_kuenstler = session.query(Kuenstler).order_by(
        Kuenstler.KuenstlerId).all()
    kuenstler = []

    for n in all_kuenstler:
        is_connected = 0
        for i in connected_kuenstler:
            if n.KuenstlerId == i.KuenstlerId:
                is_connected = 1
        if is_connected == 0:
            kuenstler.append(n)

    if request.method == 'POST':
        print("f")
        if add_lied_kuenstler_form.validate_on_submit():
            print(add_lied_kuenstler_form.CheckedCheckboxes.data)
            kuenstler_ids_to_add = list(add_lied_kuenstler_form.CheckedCheckboxes.data.split(","))
            print("data is valid")
            # new_manager.ManagerId = add_manager_form.ManagerID.data
            try:
                for i in kuenstler_ids_to_add:
                    new_Lied_Kuenstler = LiedKuenstler()
                    new_Lied_Kuenstler.KuenstlerId = int(i)
                    new_Lied_Kuenstler.LiedId = item_to_attach_id
                    db.session.add(new_Lied_Kuenstler)
                    db.session.commit()
            except ValueError:
                print("value error")
            return redirect("/lieder/edit?itemid=" + item_to_attach_id)

        else:
            return render_template(
                "liedkuenstler/liedkuenstleradd.html",
                headline="Add Lieder",
                kuenstlers=kuenstler,
                form=add_lied_kuenstler_form)

    else:
        return render_template(
            "liedkuenstler/liedkuenstleradd.html",
            headline="Add Lieder",
            kuenstlers=kuenstler,
            form=add_lied_kuenstler_form)


@lied_kuenstler_blueprint.route('/lied_kuenstler/delete', methods=["Get", "Post"])
def lied_kuenstler_delete():

    session: sqlalchemy.orm.scoping.scoped_session = db.session
    item_to_attach_id = request.args["itemid"]
    connected_kuenstler = session.query(LiedKuenstler).filter(
        LiedKuenstler.LiedId == item_to_attach_id).all()
    kuenstler = []
    try:
        for i in connected_kuenstler:
            kuenstler.append(session.query(Kuenstler).filter(
                Kuenstler.KuenstlerId == i.KuenstlerId).first())
    except AttributeError:
        kuenstler = session.query(Kuenstler).order_by(
            Kuenstler.KuenstlerId).all()

    del_form = deleteLiedKuenstlerForm()

    if request.method == 'POST':
        print("f")
        if del_form.validate_on_submit():
            delete_id_string = del_form.CheckedCheckboxes.data
            delete_id_list = list(delete_id_string.split(","))

            print(del_form.CheckedCheckboxes.data)
            for i in delete_id_list:
                print("deleting now data with id " + i)
                itemToDelete = db.session.query(LiedKuenstler).filter(
                    sqlalchemy.and_(
                        LiedKuenstler.LiedId == item_to_attach_id,
                        LiedKuenstler.KuenstlerId == i))
                itemToDelete.delete()
                db.session.commit()
                print("deleted data with id " + i)

            return redirect("/lieder/edit?itemid=" + item_to_attach_id)
        else:
            return render_template(
                "liedkuenstler/liedkuenstlerdelete.html",
                headline="Add Lieder",
                kuenstlers=kuenstler,
                form=del_form)

    else:
        return render_template(
            "liedkuenstler/liedkuenstlerdelete.html",
            headline="Add Lieder",
            kuenstlers=kuenstler,
            form=del_form)

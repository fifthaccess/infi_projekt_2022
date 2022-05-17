
from flask_wtf import FlaskForm

from wtforms.fields.simple import StringField,  HiddenField
from wtforms.fields import DecimalField,  SelectField


class KuenstlerForm(FlaskForm):
    KuenstlerId = HiddenField("KuenstlerId")
    ManagerID = DecimalField("ManagerID")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Herkunftsland = StringField("Herkunftsland")
    Gehalt = DecimalField("Gehalt")


class UserDetails(FlaskForm):
    group_id = SelectField('Group')

    # session : sqlalchemy.orm.scoping.scoped_session = db.session
    # managers = session.query(Manager).order_by(Manager.ManagerId).all

    # form.group_id.choices = [(g.Vorname.data , g.Nachname.data) for g in managers]


class DeleteKuenstlerForm(FlaskForm):
    CheckedCheckboxes = HiddenField("CheckedCheckboxes")


class editKuenstlerForm(FlaskForm):
    KuenstlerId = HiddenField("KuenstlerId")
    ManagerID = DecimalField("ManagerID")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Herkunftsland = StringField("Herkunftsland")
    Gehalt = DecimalField("Gehalt")

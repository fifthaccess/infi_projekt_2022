from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class ManagerForm(FlaskForm):
    ManagerID = HiddenField("ManagerID")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Firma = StringField("Firma")
    Kuenstler_anzahl = DecimalField("Kuenstler_anzahl")


class DeleteManagerFrom(FlaskForm):
    CheckedCheckboxes = HiddenField("CheckedCheckboxes")


class editManagerForm(FlaskForm):
    ManagerID = HiddenField("ManagerID")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Firma = StringField("Firma")
    Kuenstler_anzahl = DecimalField("Kuenstler_anzahl")

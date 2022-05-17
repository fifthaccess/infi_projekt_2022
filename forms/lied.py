from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class LiedForm(FlaskForm):
    LiedId = HiddenField("LiedId")
    Kuenstleranzahl = DecimalField("Kuenstleranzahl")
    Liedname = StringField("Liedname")
    Erscheinungsdatum = DateField("Erscheinungsdatum")


class DeleteLiederForm(FlaskForm):
    CheckedCheckboxes = HiddenField("CheckedCheckboxes")


class EditLiedForm(FlaskForm):
    LiedId = HiddenField("LiedId")
    Kuenstleranzahl = DecimalField("Kuenstleranzahl")
    Liedname = StringField("Liedname")
    Erscheinungsdatum = DateField("Erscheinungsdatum")

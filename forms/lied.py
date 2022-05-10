from operator import imod
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField 
from wtforms.fields.simple import BooleanField, StringField, TextAreaField ,HiddenField 
from wtforms.fields import DecimalField, FieldList , SelectField , DateField
from wtforms import validators
from model.models import Kuenstler
import sqlalchemy
import sqlalchemy.orm
from model.models import Manager 
from model.models import db

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
from operator import imod
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField
from wtforms import validators
from model.models import Kuenstler

class Manager(FlaskForm):
    ManagerID = StringField("ManagerID",[validators.InputRequired()])
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Firma = StringField("Firma")
    Kuenstler_anzahl = DecimalField("Kuenstler_anzahl")
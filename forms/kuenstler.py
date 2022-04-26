from operator import imod
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField 
from wtforms.fields.simple import BooleanField, StringField, TextAreaField ,HiddenField 
from wtforms.fields import DecimalField, FieldList , SelectField
from wtforms import validators
from model.models import Kuenstler
import sqlalchemy
import sqlalchemy.orm
from model.models import Manager 
from model.models import db

class KuenstlerForm(FlaskForm):
    KuenstlerId = HiddenField("KuenstlerId")
    ManagerID = HiddenField("ManagerID")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Herkunftsland = StringField("Herkunftsland")
    Gehalt = DecimalField("Gehalt")


class UserDetails(FlaskForm):
    group_id = SelectField('Group')

    #session : sqlalchemy.orm.scoping.scoped_session = db.session
    #managers = session.query(Manager).order_by(Manager.ManagerId).all
    
    #form.group_id.choices = [(g.Vorname.data , g.Nachname.data) for g in managers]


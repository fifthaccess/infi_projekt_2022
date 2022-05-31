from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField
from wtforms.fields import DecimalField


class LiedKuenstlerForm(FlaskForm):
    Id = HiddenField("Id")
    KuenstlerId = DecimalField("KuenstlerId")
    LiedId = DecimalField("LiedId")
    CheckedCheckboxes = HiddenField("CheckedCheckboxes")


class deleteLiedKuenstlerForm(FlaskForm):
    CheckedCheckboxes = HiddenField("CheckedCheckboxes")

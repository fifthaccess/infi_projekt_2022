from flask import Flask
from models import Kuenstler,Lied,LiedKuenstler,Manager,db
from flask.templating import render_template
from addItemForm import AddItemForm
app = Flask(__name__)
app.secret_key = "fifth"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Projekt_06"

db.init_app(app)
@app.route("/", methods=["get","post"])
def index():
    addItemFormObject = AddItemForm()
    items = db.session.query(Lied).all()
    return render_template("index.html", headline="Todo Items", form = addItemFormObject, items = items)
    

app.run(debug=True)
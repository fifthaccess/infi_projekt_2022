from flask import Flask
from model.models import Kuenstler,Lied,LiedKuenstler,Manager,db
from flask.templating import render_template
#from addItemForm import AddItemForm
from controllers.index import index_blueprint
from controllers.manager import manager_blueprint
app = Flask(__name__)
app.secret_key = "fifth"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Projekt_06"

db.init_app(app)
#@app.route("/", methods=["get","post"])
#def index():
#    items = db.session.query(Lied).all()
#    return render_template("index.html", headline="Übersicht")#, form = addItemFormObject, items = items)
    
app.register_blueprint(index_blueprint)
app.register_blueprint(manager_blueprint)
if __name__ == "__main__": 
    app.run(debug=True)     
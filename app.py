from flask import Flask
from model.models import db
from flask.templating import render_template
#from addItemForm import AddItemForm
from controllers.index import index_blueprint
from controllers.manager import manager_blueprint
from controllers.kuenstler import kuenstler_blueprint
from controllers.lied import lied_blueprint
app = Flask(__name__)
app.secret_key = "fifth"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Projekt_06"

db.init_app(app)

app.register_blueprint(index_blueprint)
app.register_blueprint(manager_blueprint)
app.register_blueprint(kuenstler_blueprint)
app.register_blueprint(lied_blueprint)
if __name__ == "__main__": 
    app.run(debug=True)     
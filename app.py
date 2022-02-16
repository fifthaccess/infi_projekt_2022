from flask import Flask
from model import Todoitem, db
app = Flask(__name__)
app.secret_key = "fifth0"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Projekt_06"
db.init_app(app)

#test = Todoitem
#test.__tablename__ = "test "
@app.route("/", methods=["get","post"])
def index():
    
from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    session
)
from pymongo import MongoClient
from bson.objectid import ObjectId
from functools import wraps
import os

from forms import ChallengeForm, RegisterForm

# ----------------------
# APP CONFIG
# ----------------------
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret")

# ----------------------
# MONGO CONNECTION
# ----------------------
MONGO_URI = os.getenv("MONGO_URI_IN", os.getenv("MONGO_URI"))
client = MongoClient(MONGO_URI)
db = client["dev_challenges"]

# Crear admin si no existe
if db.users.count_documents({"username": "admin"}) == 0:
    db.users.insert_one({
        "username": "admin",
        "password": "admin",
        "role": "admin"
    })
    print("Admin creado automáticamente")

# ----------------------
# DECORATORS
# ----------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# ----------------------
# REGISTER
# ----------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if db.users.find_one({"username": form.username.data}):
            return "El usuario ya existe"

        db.users.insert_one({
            "username": form.username.data,
            "password": form.password.data,
            "role": "user"
        })

        return redirect(url_for("login"))

    return render_template("register.html", form=form)

# ----------------------
# LOGIN
# ----------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.users.find_one({
            "username": request.form["username"],
            "password": request.form["password"]
        })

        if user:
            session["user"] = user["username"]
            session["role"] = user.get("role", "user")
            return redirect(url_for("index"))

    return render_template("login.html")

# ----------------------
# LOGOUT
# ----------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ----------------------
# DASHBOARD
# ----------------------
@app.route("/")
def index():
    total = db.challenges.count_documents({})

    pipeline = [
        {
            "$group": {
                "_id": "$language",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    language_stats = list(db.challenges.aggregate(pipeline))

    my_total = 0
    if session.get("user"):
        my_total = db.challenges.count_documents({
            "author": session.get("user")
        })

    return render_template(
        "inicio.html",
        total=total,
        language_stats=language_stats,
        my_total=my_total
    )

# ----------------------
# READ
# ----------------------
@app.route("/challenges")
def read_challenges():
    language = request.args.get("language")
    my = request.args.get("my")

    query = {}

    if language:
        query["language"] = language

    if my == "1" and session.get("user"):
        query["author"] = session.get("user")

    challenges = list(db.challenges.find(query))

    return render_template(
        "read.html",
        challenges=challenges,
        language=language,
        my=my
    )

# ----------------------
# CREATE
# ----------------------
@app.route("/challenges/add", methods=["GET", "POST"])
@login_required
def add_challenge():
    form = ChallengeForm()

    if form.validate_on_submit():
        challenge = {
            "title": form.title.data,
            "language": form.language.data,
            "level": form.level.data,
            "description": form.description.data,
            "solution": form.solution.data,
            "author": session.get("user")
        }

        db.challenges.insert_one(challenge)

        return redirect(url_for("read_challenges"))

    return render_template("add.html", form=form)

# ----------------------
# UPDATE
# ----------------------
@app.route("/challenges/edit/<id>", methods=["GET", "POST"])
@login_required
def edit_challenge(id):
    challenge = db.challenges.find_one({"_id": ObjectId(id)})

    if not challenge:
        return "Reto no encontrado", 404

    if challenge.get("author") != session.get("user") and session.get("role") != "admin":
        return "No tienes permiso para editar este reto", 403

    form = ChallengeForm(data=challenge)

    if form.validate_on_submit():
        db.challenges.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "title": form.title.data,
                "language": form.language.data,
                "level": form.level.data,
                "description": form.description.data,
                "solution": form.solution.data
            }}
        )

        return redirect(url_for("read_challenges"))

    return render_template("update.html", form=form)

# ----------------------
# DELETE
# ----------------------
@app.route("/challenges/delete/<id>")
@login_required
def delete_challenge(id):
    challenge = db.challenges.find_one({"_id": ObjectId(id)})

    if not challenge:
        return "Reto no encontrado", 404

    if challenge.get("author") != session.get("user") and session.get("role") != "admin":
        return "No tienes permiso para borrar este reto", 403

    db.challenges.delete_one({"_id": ObjectId(id)})

    return redirect(url_for("read_challenges"))

# ----------------------
# DETAIL
# ----------------------
@app.route("/challenges/<id>")
def challenge_detail(id):
    challenge = db.challenges.find_one({"_id": ObjectId(id)})

    if not challenge:
        return "Reto no encontrado", 404

    return render_template("detail.html", challenge=challenge)

# ----------------------
# MAIN
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)

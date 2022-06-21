import re
import sys

from flask import redirect, render_template, request, session, url_for

from app import app
from app.models import login_model
from app.views import index_view


@app.route("/")
def index():
    view = index_view.index_view()
    template = view.getTemplateName()
    return render_template(template)


@app.route("/registrar")
def registrar():
    return render_template("registro.html")


@app.route("/registraUsuario", methods=["POST"])
def registraUsuario():
    # Nuestra expresión regular de contraseñas
    regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"  # noqa W605
    # Instanciamos modelo login que sirve para login y registro
    model = login_model.login_model()
    # Obtenemos la información enviada por POST
    # de nuestra form. Se maneja como un diccionario
    # e.g data["nombre"]
    data = request.form
    # Obtenemos campos de este diccionario
    print(data, "\n\n\n", file=sys.stderr)
    nombre = data.get("nombre")
    correo = data.get("correo")
    password = data.get("password")
    confirmaPassword = data.get("confirmaPassword")
    username = data.get("username")
    # Validamos que existan todos los campos
    if (
        not nombre or not correo or not password or not confirmaPassword or not username
    ):  # noqa
        redirect(url_for("registrar"))
        return render_template(
            "registro.html", errorMsg="Error: llena todos los campos."
        )  # noqa E501
    # Validamos que contraseña tenga formato correcto
    passwordValida = re.search(regexp, password)
    if not passwordValida:
        redirect(url_for("registrar"))
        return render_template(
            "registro.html",
            errorMsg="Error: la contraseña debe de ser de mínimo 8 caractéres, tener una letra mayúscula, minúscula y  un número.",  # noqa E501
        )
    if password != confirmaPassword:
        redirect(url_for("registrar"))
        return render_template(
            "registro.html", errorMsg="Error: las contraseñas no son iguales."
        )
    # Veamos si ya existe este usuario
    doesUserExist = model.doesUserExist(username)
    if doesUserExist:
        redirect(url_for("registrar"))
        return render_template(
            "registro.html", errorMsg="Error: ya existe este usuario: " + username + "."
        )
    registroExitoso = model.registerUser(
        nombre, correo, password, confirmaPassword, username
    )
    if registroExitoso:
        """data={"success":"true",
        "usuario":session.get("correo")}
        return redirect(url_for("registrar"))"""
        return render_template(
            "registro.html",
            confirmMsg="Revisa tu correo para confirmarlo"
            + " y después podrás hacer login.",  # noqa E501
        )
    else:
        redirect(url_for("registrar"))
        return render_template(
            "registro.html", errorMsg="Error: registrando usuario."
        )  # noqa E501


@app.route("/login", methods=["POST"])
def login():
    model = login_model.login_model()
    data = request.form
    user = data["correo"]
    password = data["password"]
    doesUserExist, msg = model.loginUser(user, password)
    if doesUserExist:
        return redirect(url_for("main"))
    else:
        redirect(url_for("index"))
        return render_template("index.html", errorMsg="ERROR: " + msg)


@app.route("/main")
def main():
    if session.get("id") is None:
        return redirect(url_for("index"))
    else:
        return render_template("main.html")


@app.route("/logout")
def logout():
    if session.get("id") is None:
        redirect("index.html")
        return redirect(url_for("index"))
    else:
        session.pop("id", None)
        session.pop("nombre", None)
        session.pop("correo", None)
        return redirect(url_for("index"))

@app.route("/tweets/new", methods=["POST"])
def generarTweet():
    # Instanciamos el objeto de tweet_model.
    model = tweet_model.tweet_model()
    # Obtenemos la información enviada por POST
    # de nuestra form. Se maneja como un diccionario
    # e.g data["nombre"]
    data = request.form

    # Obtenemos campos de este diccionario
    print(data, "\n\n\n", file=sys.stderr)

    # Verificamos contenido del tweet.
    if data["tweet"] == "" or len(data["tweet"]) > 512:
        print("Tweet invalido, debe tener entre 1 y 512 caracteres.")
        return "Error en tweet"

    # Request entry to DB.
    model.sendTweet(data["tweet"])

    return redirect(url_for("index"))

@app.route("/tweets/<id>/edit", methods=["PATCH"])
def editarTweet():
    model = tweet_model.tweet_model()
    data = request.form

    # Obtenemos campos de este diccionario
    print(data, "\n\n\n", file=sys.stderr)

    # Verificamos contenido del tweet.
        if data["tweet"] == "" or len(data["tweet"]) > 512:
        print("Tweet invalido, debe tener entre 1 y 512 caracteres.")
        return "Error en tweet"

    # Request entry to DB.
    model.modifyTweet(data["tweet"], id)
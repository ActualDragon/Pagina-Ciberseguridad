import sys

from flask import redirect, render_template, request, session, url_for

from app import app
from app.models import login_model
from app.views import index_view
import re

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
    regexp="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    # Instanciamos modelo login que sirve para login y registro
    model = login_model.login_model()
    # Obtenemos la información enviada por POST
    # de nuestra form. Se maneja como un diccionario
    # e.g data["nombre"]
    data = request.form
    # Obtenemos campos de este diccionario
    print(data, "\n\n\n", file=sys.stderr)
    nombre = data["nombre"]
    correo = data["correo"]
    password = data["password"]
    confirmaPassword = data["confirmaPassword"]
    # Validamos que contraseña tenga formato correcto
    passwordValida=re.search(regexp, password)
    if not passwordValida:
        redirect(url_for("registrar"))
        return render_template(
            "registro.html", errorMsg="Error: la contraseña debe de ser de mínimo 8 caractéres, tener una letra mayúscula, minúscula y  un número."
        )  # noqa E501
    if password!=confirmaPassword:
        redirect(url_for("registrar"))
        return render_template(
            "registro.html", errorMsg="Error: las contraseñas no son iguales."
        )
    username = data["username"]
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
            + "y después podrás hacer login.",  # noqa E501
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
    doesUserExist = model.loginUser(user, password)
    if doesUserExist:
        data = {"success": "true", "usuario": session.get("correo")}
        return redirect(url_for("main"))
    else:
        redirect(url_for("index"))
        return render_template("index.html", errorMsg="Error: Error de Login.")


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

from flask import render_template
from flask import request, session, redirect, jsonify, url_for
from app import app
from app.models import  login_model, mispacientes_model, perfil_model
from app.views import index_view, blog_view, pacientes_view, perfil_view, paciente_view
import sys
@app.route('/')
def index():
    view= index_view.index_view()
    template=view.getTemplateName()
    return render_template(template)
@app.route('/registrar')
def registrar():
    return render_template("registro.html")
@app.route('/registraUsuario', methods=["POST"])
def registraUsuario():
    #Instanciamos modelo login que sirve para login y registro
    model=login_model.login_model()
    #Obtenemos la información enviada por POST
    #de nuestra form. Se maneja como un diccionario 
    #e.g data["nombre"]
    data=request.form
    #Obtenemos campos de este diccionario
    nombre=data["nombre"]
    correo=data["correo"]
    password=data["password"]
    confirmaPassword=data["confirmaPassword"]
    
    registroExitoso=model.registerUser(nombre,correo, password, confirmaPassword)
    if registroExitoso:
        '''data={"success":"true",
        "usuario":session.get("correo")}
        return redirect(url_for("registrar"))'''
        return render_template("registro.html", confirmMsg="Revisa tu correo para confirmarlo, y después podrás hacer login.")
    else:
        redirect(url_for('registrar'))
        return render_template("registro.html", errorMsg="Error: registrando usuario.")
@app.route('/login', methods=["POST"])
def login():
    model=login_model.login_model()
    data=request.form
    user=data["email"]
    password=data["password"]
    doesUserExist=model.loginUser(user, password)
    if doesUserExist:
        data={"success":"true",
        "usuario":session.get("correo")}
        return redirect(url_for("main"))
    else:
        redirect(url_for('index'))
        return render_template("index.html", errorMsg="Error: combinación usuario/contraseña incorrecta.")
@app.route('/main')
def main():
    if session.get("id") is None:
        return redirect(url_for('index'))
    else:
        return render_template("main.html")
@app.route('/logout')
def logout():
    if session.get("id") is None:
        redirect("index.html")
        return redirect(url_for('index'))
    else:
        session.pop("id",None)
        session.pop("nombre",None)
        session.pop("correo",None)
        return redirect(url_for('index'))
@app.route('/blog')
def blog():
    view=blog_view.blog_view()
    return render_template(view.getTemplateName())
@app.route('/pacientes')
def pacientes():
    model= mispacientes_model.mispacientes_model()
    view=pacientes_view.pacientes_view()
    pacientes=model.getPacientes(session.get("id"))
    filas=view.llenarTabla(pacientes)
    
    return render_template(view.getTemplateName(), filas=filas)
@app.route('/perfil')
def perfil():
    view=perfil_view.perfil_view()
    model=perfil_model.perfil_model()
    datos=model.getDatosPerfil(session.get("id"))
    return render_template(view.getTemplateName(), perfil=datos)
@app.route('/actualizarEspecializacion', methods=["POST"])
def actualizarEspecializacion():
    view=perfil_view.perfil_view()
    model=perfil_model.perfil_model()
    data=request.form
    especializacion=data["especializacion"]
    model.actualizarEspecializacion(session.get("id"), especializacion)
    datos=model.getDatosPerfil(session.get("id"))
    return redirect(url_for("main"))
@app.route('/actualizarInstitucion', methods=["POST"])
def actualizarInstitucion():
    view=perfil_view.perfil_view()
    model=perfil_model.perfil_model()
    data=request.form
    institucion=data["institucion"]
    pais=data["pais"]
    estado=data["estado"]
    model.actualizarInstitucion(session.get("id"), institucion, pais, estado)
    datos=model.getDatosPerfil(session.get("id"))
    return redirect(url_for("main"))
    #return render_template(view.getTemplateName(), perfil=datos, msgExitoI="¡Se han actualizado los cambios!")
@app.route('/getPaciente', methods=["POST"])
def getPaciente():
    model=mispacientes_model.mispacientes_model()
    data=request.form
    id=data["idPaciente"]
    paciente=model.getPacienteByID(id,session.get("id"))
    return jsonify(paciente)
@app.route('/verPaciente')
def verPaciente():
    view=paciente_view.paciente_view()
    return render_template(view.getTemplateName())
@app.route('/modificarPaciente', methods=["POST"])
def modificarPaciente():
    model=mispacientes_model.mispacientes_model()
    data=request.form
    id=data["id"]
    peso=data["peso"]
    estatura=data["estatura"]
    diagnostico=data["diagnostico"]
    actualizar=model.modificarPaciente(session.get('id'),id,peso,estatura,diagnostico)
    redirect(url_for("main"))
    response={"success":actualizar}
    return jsonify(response)
@app.route('/verArticulo')
def verArticulo():
    view=blog_view.blog_view()
    return render_template(view.getTemplateNameArticulo())

@app.route('/verArticuloQueEs')
def verArticuloQueEs():
    view=blog_view.blog_view()
    return render_template(view.getArticuloQueEs())

@app.route('/verArticuloConsultaPacientes')
def verArticuloConsultaPacientes():
    view=blog_view.blog_view()
    return render_template(view.getArticuloConsultaPacientes())

@app.route('/verArticuloAnalizaMovimiento')
def verArticuloAnalizaMovimiento():
    view=blog_view.blog_view()
    return render_template(view.getArticuloAnalizaMovimiento())

@app.route('/verArticuloModeloPredictivo')
def verArticuloModeloPredictivo():
    view=blog_view.blog_view()
    return render_template(view.getArticuloModeloPredictivo())
@app.route('/verArticuloConectaApp')
def verArticuloConectaApp():
    view=blog_view.blog_view()
    return render_template(view.getArticuloConectaApp())
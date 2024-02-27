from flask import Flask, render_template,request,Response
import forms

from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash
from config import DevelopmentConfig
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


csrf=CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.route("/index",methods=["GET", "POST"])
def index():
    alum_form=forms.UserForm2(request.form)
    if request.method == "POST" and alum_form.validate():
        alum=Alumnos(nombre=alum_form.nombre.data,
                 apaterno=alum_form.apaterno.data,
                 email=alum_form.email.data)
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form=alum_form)

@app.route("/ABC_Complemento", methods=["GET", "POST"])
def ABCompleto():
    alum_form=forms.UserForm2(request.form)
    alumno=Alumnos.query.all()
    return render_template("ABC_Completo.html", alumno=alumno)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    
    nom=""
    apaterno=""
    correo=""
    alum_form=forms.UserForm(request.form)
    if request.method == "POST" and alum_form.validate():
        nom = alum_form.nombre.data
        correo = alum_form.email.data
        apaterno = alum_form.apaterno.data
        mensaje='Bienvenido: {}'.format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom))
        print("correo: {}".format(correo))
        print("apaterno: {}".format(apaterno))
    return render_template("alumnos.html", form=alum_form, nom=nom, apaterno=apaterno,correo=correo)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
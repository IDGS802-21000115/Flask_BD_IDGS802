from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField
from wtforms import EmailField
from wtforms import validators

 
class UserForm(Form):
    nombre = StringField("nombre",[validators.DataRequired(message='el campo es requerido'), validators.Length(min=4,max=10,message='ingresa nombre valido')])
    email = EmailField("materno")
    apaterno = StringField("apaterno")
    edad=IntegerField('edad',[validators.number_range(min=1,max=20,message='valor no valido')])
    materias = SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingles','Ing')])
    radios = RadioField('Curso',choices=[("1", "1"),("2", "2"),("3", "3")])
    correo=EmailField('correo',[validators.Email(message='Ingrese un correo valido')])
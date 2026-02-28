from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms import PasswordField

class ChallengeForm(FlaskForm):
    title = StringField("Título", validators=[DataRequired()])
    language = SelectField("Lenguaje", choices=[
        ("Python", "Python"),
        ("Java", "Java"),
        ("JavaScript", "JavaScript"),
        ("C#", "C#"),
        ("SQL", "SQL")
    ])
    level = SelectField("Nivel", choices=[
        ("Básico", "Básico"),
        ("Intermedio", "Intermedio"),
        ("Avanzado", "Avanzado")
    ])
    description = TextAreaField("Descripción", validators=[DataRequired()])
    solution = TextAreaField("Solución", validators=[DataRequired()])
    submit = SubmitField("Guardar")

class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

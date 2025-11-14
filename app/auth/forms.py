from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models.user import User

msg_obg = 'Esse campo é obrigatório!'

class LoginForm(FlaskForm):
    username  = StringField('Usuário ou Email', validators=[DataRequired(message=msg_obg)])
    password = PasswordField('Senha', validators=[DataRequired(message=msg_obg)])
    submit = SubmitField('Entrar')
    
class RegistrationForm(FlaskForm):
    name = StringField('Nome Completo', validators=[DataRequired(message=msg_obg)])
    username = StringField('Nome de Usuário', validators=[DataRequired(message=msg_obg)])
    email = StringField('Email', validators=[DataRequired(message=msg_obg), Email()])
    password = PasswordField('Senha', validators=[DataRequired(message=msg_obg), Length(min=6)])
    password_confirm = PasswordField('Repita a senha', validators=[DataRequired(message=msg_obg), EqualTo('password')])
    submit = SubmitField('Registrar')
    
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Nome de usuário já existe.')
        
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email já registrado.')
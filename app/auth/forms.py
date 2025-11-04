from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models.user import User

class LoginForm(FlaskForm):
    username  = StringField('Usuário ou Email', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')
    
class RegistrationForm(FlaskForm):
    name = StringField('Nome Completo', validators=[DataRequired()])
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')
    
    def validate_on_submit(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Nome de usuário já existe.')
        
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email já registrado.')
"""
Formularios de la aplicación Gear4Music
Contiene los formularios WTForms para instrumentos, usuarios y autenticación
"""

import re
from wtforms import Form, SelectField, StringField, SubmitField, ValidationError, validators, PasswordField
from databases.db import User


# =============================================================================
# FORMULARIO DE INSTRUMENTOS
# =============================================================================

class InstrumentForm(Form):
    """Formulario para crear/editar instrumentos"""
    name = StringField('Name', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
    ])
    category_id = SelectField('Category', [validators.DataRequired()], choices=[], coerce=int)
    supplier_id = SelectField('Supplier', [validators.DataRequired()], choices=[], coerce=int)
    image = StringField('Image', [validators.length(min=4, max=500)])
    image_2 = StringField('Image 2', [validators.length(min=4, max=500)])
    submit = SubmitField('Save')


# =============================================================================
# FORMULARIOS DE AUTENTICACIÓN
# =============================================================================

class UserForm(Form):
    """Formulario de inicio de sesión"""
    name = StringField('Name', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
    ], render_kw={"placeholder": "Name"})
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
    ], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')


class RegisterForm(Form):
    """Formulario de registro de usuarios"""
    name = StringField('Name', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
    ], render_kw={"placeholder": "Name"})
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
    ], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')
    
    def validate_name(self, field):
        """Validar que el nombre de usuario no contenga caracteres prohibidos ni exista"""
        forbidden_chars = r'[%\s"\\\/]'
        if re.search(forbidden_chars, field.data):
            raise ValidationError('Username cannot contain %, spaces, quotes, backslashes, or slashes.')
        
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('That username already exists. Please choose a different one.')


# =============================================================================
# FORMULARIO DE PERFIL
# =============================================================================

class ChangePasswordForm(Form):
    """Formulario para cambiar contraseña"""
    current_password = PasswordField('Current Password', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
    ])
    new_password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
    ])
    confirm_password = PasswordField('Confirm Password', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
    ])
    submit = SubmitField('Change Password')
    
    def validate_new_password(self, field):
        """Validar que la contraseña no contenga caracteres peligrosos"""
        forbidden_chars = r'[\'";\\<>]'
        if re.search(forbidden_chars, field.data):
            raise ValidationError('Password cannot contain quotes, semicolons, backslashes, or angle brackets.')
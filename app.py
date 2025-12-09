"""
Gear4Music Flask Application
Aplicación principal con gestión de usuarios y instrumentos
"""

from flask import Flask, render_template, abort, redirect, request, url_for
from databases.db import db, Instrument, Category, Supplier, User
from forms.task_form import InstrumentForm, UserForm, RegisterForm, ChangePasswordForm
import config as custom_config
from functools import wraps
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_bcrypt import Bcrypt


# =============================================================================
# DECORADORES PERSONALIZADOS
# =============================================================================

def admin_required(f):
    """Requiere rol de administrador para acceder a la ruta"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


# =============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# =============================================================================

app = Flask(__name__)
app.config.from_object(custom_config)
app.config['SECRET_KEY'] = '1234'
db.init_app(app)
bcrypt = Bcrypt(app)

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))  # Optimizado: usar .get() en lugar de filter_by

@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauthorized.html')


# =============================================================================
# AUTENTICACIÓN
# =============================================================================

@app.route('/', methods=['GET', 'POST'])
def login():
    """Página de inicio de sesión"""
    form = UserForm(request.form)
    if form.validate() and request.method == "POST":
        user = User.query.filter_by(name=form.name.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('hello'))
        form.name.errors.append("Incorrect user or password")
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Registro de nuevos usuarios"""
    form = RegisterForm(request.form)
    if form.validate() and request.method == "POST":
        new_user = User(
            name=form.name.data,
            password=bcrypt.generate_password_hash(form.password.data)
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)  # Auto-login después de registro
        return redirect(url_for('hello'))
    return render_template('register.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    """Cerrar sesión"""
    logout_user()
    return redirect(url_for('login'))


# =============================================================================
# PERFIL DE USUARIO
# =============================================================================

@app.route('/profile/')
@login_required
def profile():
    """Página de perfil del usuario"""
    return render_template('profile.html', form=ChangePasswordForm())


@app.route('/profile/change-password/', methods=['POST'])
@login_required
def change_password():
    """Cambiar contraseña del usuario"""
    form = ChangePasswordForm(request.form)
    success = False
    
    if form.validate():
        if not bcrypt.check_password_hash(current_user.password, form.current_password.data):
            form.current_password.errors.append("Current password is incorrect")
        elif form.new_password.data != form.confirm_password.data:
            form.confirm_password.errors.append("Passwords do not match")
        else:
            current_user.password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            db.session.commit()
            success = True
    
    return render_template('profile.html', form=form, success=success)


# =============================================================================
# PÁGINAS PRINCIPALES
# =============================================================================

@app.route('/index/')
@login_required
def hello():
    """Página principal"""
    return render_template('index.html')


@app.route('/contact/')
@login_required
def contact():
    """Página de contacto"""
    return render_template('contact.html')


# =============================================================================
# GESTIÓN DE INSTRUMENTOS
# =============================================================================

@app.route('/instrumentos/')
@login_required
def intrumentos():
    """Lista de todos los instrumentos"""
    return render_template('instrumentos.html', instruments=Instrument.query.all())


@app.route('/instrument/<int:id>/details/')
@login_required
def details(id):
    """Detalles de un instrumento"""
    instrument = Instrument.query.get_or_404(id)  # Optimizado: usar get_or_404
    return render_template('details.html', instrument=instrument)


@app.route('/instrument/<int:id>/delete/')
@login_required
@admin_required
def delete(id):
    """Eliminar un instrumento (solo admin)"""
    instrument = Instrument.query.get_or_404(id)
    db.session.delete(instrument)
    db.session.commit()
    return redirect('/instrumentos/')


@app.route('/instrument/<int:id>/update/', methods=["GET", "POST"])
@login_required
@admin_required
def update(id):
    """Actualizar un instrumento (solo admin)"""
    instrument = Instrument.query.get_or_404(id)
    form = InstrumentForm(request.form, obj=instrument)
    
    # Cargar opciones de selects
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    form.supplier_id.choices = [(s.id, s.name) for s in Supplier.query.all()]

    if form.validate() and request.method == "POST":
        instrument.name = form.name.data
        instrument.category_id = form.category_id.data
        instrument.supplier_id = form.supplier_id.data
        instrument.image = form.image.data
        instrument.image_2 = form.image_2.data
        db.session.commit()
        return redirect('/instrumentos/')
    
    return render_template('update_instrument.html', form=form)


@app.route('/instrument/create/', methods=['GET', 'POST'])
@login_required
@admin_required
def create():
    """Crear nuevo instrumento (solo admin)"""
    form = InstrumentForm(request.form)
    
    # Cargar opciones de selects
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    form.supplier_id.choices = [(s.id, s.name) for s in Supplier.query.all()]
    
    if form.validate() and request.method == "POST":
        instrument = Instrument(
            name=form.name.data,
            category_id=form.category_id.data,
            supplier_id=form.supplier_id.data,
            image=form.image.data,
            image_2=form.image_2.data
        )
        db.session.add(instrument)
        db.session.commit()
        return redirect('/instrumentos/')
    
    return render_template('create_instrument.html', form=form)


# =============================================================================
# BÚSQUEDA
# =============================================================================

@app.route('/search')
@login_required
def search():
    """Búsqueda de instrumentos"""
    query = request.args.get('query', '')
    instruments = []
    
    # Validar query para prevenir inyección
    if query and '%' not in query and ' ' not in query:
        instruments = Instrument.query.filter(Instrument.name.ilike(f'%{query}%')).all()
    
    return render_template('search_results.html', instruments=instruments, query=query)

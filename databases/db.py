"""
Modelos de base de datos para Gear4Music
Define las tablas: Category, Supplier, Instrument, User
"""

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


# =============================================================================
# MODELOS
# =============================================================================

class Category(db.Model):
    """Categorías de instrumentos"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<Category {self.id}: {self.name}>'


class Supplier(db.Model):
    """Proveedores de instrumentos"""
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<Supplier {self.id}: {self.name}>'


class Instrument(db.Model):
    """Instrumentos musicales"""
    __tablename__ = 'instruments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image = Column(String(200), nullable=True)
    image_2 = Column(String(200), nullable=True)
    
    # Relaciones
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    supplier = relationship('Supplier', backref='instruments')
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', backref='instruments')

    def __repr__(self):
        return f'<Instrument {self.id}: {self.name}>'


class User(db.Model, UserMixin):
    """Usuarios del sistema"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    role = Column(String(20), nullable=False, default='client')  # 'admin' o 'client'

    def __repr__(self):
        return f'<User {self.id}: {self.name}>'

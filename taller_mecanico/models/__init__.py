from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehiculo(db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, primary_key=True)
    propietario = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    servicios = db.relationship('Servicio', backref='vehiculo', lazy=True)

class Servicio(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    costo = db.Column(db.Float, nullable=False)

class Refaccion(db.Model):
    __tablename__ = 'refacciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    modelo_compatible = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    garantia = db.Column(db.Boolean, nullable=False)

from flask import Flask, render_template
from models import db, Vehiculo  # Importamos los modelos necesarios
from routes import vehiculos  # Importamos el blueprint de vehiculos

# Inicializamos la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taller.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

# Registrar el blueprint para manejar las rutas relacionadas con vehículos
app.register_blueprint(vehiculos, url_prefix='/')

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Prueba para listar vehículos y mostrarlos en la terminal (opcional)
with app.app_context():
    vehiculos = Vehiculo.query.all()
    for vehiculo in vehiculos:
        print(f"ID: {vehiculo.id}, Propietario: {vehiculo.propietario}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}")

# Bloque principal para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

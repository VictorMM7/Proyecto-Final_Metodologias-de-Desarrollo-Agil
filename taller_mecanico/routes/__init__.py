from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Vehiculo, Servicio, Refaccion
from datetime import datetime

vehiculos = Blueprint('vehiculos', __name__)

@vehiculos.route('/vehiculos', methods=['GET'])
def listar_vehiculos():
    lista_vehiculos = Vehiculo.query.all()
    return render_template('listar_vehiculos.html', vehiculos=lista_vehiculos)

@vehiculos.route('/vehiculos/agregar', methods=['GET', 'POST'])
def agregar_vehiculo():
    if request.method == 'POST':
        propietario = request.form['propietario']
        marca = request.form['marca']
        modelo = request.form['modelo']
        anio = int(request.form['anio'])
        nuevo_vehiculo = Vehiculo(
            propietario=propietario,
            marca=marca,
            modelo=modelo,
            anio=anio
        )
        db.session.add(nuevo_vehiculo)
        db.session.commit()
        return redirect(url_for('vehiculos.listar_vehiculos'))
    return render_template('agregar_vehiculo.html')

@vehiculos.route('/vehiculos/editar/<int:id>', methods=['GET', 'POST'])
def editar_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    if request.method == 'POST':
        vehiculo.propietario = request.form['propietario']
        vehiculo.marca = request.form['marca']
        vehiculo.modelo = request.form['modelo']
        vehiculo.anio = int(request.form['anio'])
        db.session.commit()
        return redirect(url_for('vehiculos.listar_vehiculos'))
    return render_template('editar_vehiculo.html', vehiculo=vehiculo)

@vehiculos.route('/vehiculos/eliminar/<int:id>', methods=['POST'])
def eliminar_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return redirect(url_for('vehiculos.listar_vehiculos'))

@vehiculos.route('/servicios/<int:vehiculo_id>', methods=['GET'])
def listar_servicios(vehiculo_id):
    vehiculo = Vehiculo.query.get_or_404(vehiculo_id)
    servicios = Servicio.query.filter_by(vehiculo_id=vehiculo_id).all()
    return render_template('listar_servicios.html', vehiculo=vehiculo, servicios=servicios)

@vehiculos.route('/servicios/agregar/<int:vehiculo_id>', methods=['GET', 'POST'])
def agregar_servicio(vehiculo_id):
    vehiculo = Vehiculo.query.get_or_404(vehiculo_id)
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
        costo = float(request.form['costo'])
        nuevo_servicio = Servicio(
            vehiculo_id=vehiculo_id,
            descripcion=descripcion,
            fecha=fecha,
            costo=costo
        )
        db.session.add(nuevo_servicio)
        db.session.commit()
        return redirect(url_for('vehiculos.listar_servicios', vehiculo_id=vehiculo_id))
    return render_template('agregar_servicio.html', vehiculo=vehiculo)

@vehiculos.route('/refacciones', methods=['GET'])
def listar_refacciones():
    refacciones = Refaccion.query.all()
    return render_template('listar_refacciones.html', refacciones=refacciones)

@vehiculos.route('/refacciones/agregar', methods=['GET', 'POST'])
def agregar_refaccion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo_compatible = request.form['modelo_compatible']
        stock = int(request.form['stock'])
        garantia = request.form['garantia'] == 'true'
        nueva_refaccion = Refaccion(
            nombre=nombre,
            modelo_compatible=modelo_compatible,
            stock=stock,
            garantia=garantia
        )
        db.session.add(nueva_refaccion)
        db.session.commit()
        return redirect(url_for('vehiculos.listar_refacciones'))
    return render_template('agregar_refaccion.html')

@vehiculos.route('/servicios', methods=['GET'])
def seleccionar_vehiculo():
    lista_vehiculos = Vehiculo.query.all()
    return render_template('seleccionar_vehiculo.html', vehiculos=lista_vehiculos)


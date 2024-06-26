from datetime import datetime
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Sucursal, Transporte, Repartidor, Paquete

@app.route('/')
def inicio():
    return render_template('inicio.html', sucursales = Sucursal.query.order_by(Sucursal.numero).all())

@app.route('/Opciones', methods = ['GET', 'POST'])
def opciones():
    session["id"] = request.form.get("sucursales")
    if session["id"]:
        return render_template('opciones.html')
    else:
        return render_template('inicio.html')

@app.route('/RegistrarPaquete', methods = ['GET', 'POST'])
def RegistrarPaquete():
    if session["id"]:
        ultimo_paquete = Paquete.query.order_by(Paquete.id.desc()).first()
        numeroenvio = ultimo_paquete.numeroenvio + 20
        nomdestinatario = request.form.get('nomdestinatario')
        peso = request.form.get('peso')
        dirdestinatario = request.form.get('dirdestinatario')
        idrepartidor = 0
        idtransporte = 0
        observaciones = 0
        idsucursal = session["id"]
        if not nomdestinatario and not peso and not dirdestinatario:
            return render_template('RegistrarPaquete.html')
        elif not nomdestinatario or not peso or not dirdestinatario:
            return render_template('aviso.html', aviso = "ERROR en el Registro de Pedido")
        else:
            nuevo_paquete = Paquete(numeroenvio = numeroenvio, peso = peso, nomdestinatario = nomdestinatario, dirdestinatario = dirdestinatario, entregado = 0 , observaciones = observaciones, idsucursal = idsucursal, idtransporte = idtransporte, idrepartidor = idrepartidor)
            db.session.add(nuevo_paquete)
            db.session.commit()
            return render_template('aviso.html', aviso = "El paquete fue cargado exitosamente")
    else: return render_template('inicio.html')

@app.route('/SeleccionarTransporte', methods = ['GET', 'POST'])
def SeleccionarTransporte():
    idsucursal = request.form.get('sucursales')
    numerotransporte = random.randint(300, 600)
    fechahorasalida = datetime.now()
    fechahorallegada = None
    if not idsucursal:
        return render_template('SeleccionarTransporte.html', sucursales = Sucursal.query.order_by(Sucursal.numero).all(), paquetes = Paquete.query.filter_by(entregado = 0, idrepartidor=0).all())
    elif not numerotransporte or not fechahorasalida:
        return render_template('aviso.html', aviso = "Error al Seleccionar Transporte")
    else: 
        nuevo_transporte = Transporte(numerotransporte = numerotransporte, fechahorasalida = fechahorasalida, fechahorallegada = fechahorallegada, idsucursal = idsucursal)
        db.session.add(nuevo_transporte)
        db.session.commit()
        paquetes_selec = request.form.getlist('paquetes_selec[]')
        for idpaquete in paquetes_selec:
            print("PAQUETE--->>>",idpaquete)
            paquete = Paquete.query.filter_by(id = idpaquete).first()
            paquete.entregado = 1
            db.session.commit()
        return render_template('aviso.html', aviso = 'Transporte Registrado correctamente')

@app.route('/LlegadaTransporte', methods = ['GET', 'POST'])
def LlegadaTransporte():
    idtransporte = request.form.get('Transportes')
    if session['id']:
        if idtransporte:
            transporte = Transporte.query.filter_by(id = idtransporte, fechahorallegada = None, idsucursal = session['id']).first()
            if transporte:
                transporte.fechahorallegada = datetime.now()
                db.session.commit()
                return render_template('aviso.html', aviso = 'Llegada registrada exitosamente')
            else:
                return render_template('aviso.html', aviso = 'Error al registrar la llegada')
    transportes = Transporte.query.filter_by(fechahorallegada = None, idsucursal = session['id']).all()
    return render_template('LlegadaTransporte.html', Transportes=transportes)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
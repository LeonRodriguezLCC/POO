from flask import Flask, render_template, request, flash, redirect
from models import db, Trabajador, RegistroHorario
from datetime import date, time, datetime


app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def inicio():
    return render_template('Inicio.html')

@app.route('/RegistraEntrada', methods = ['GET', 'POST'])
def RegistraEntrada():
    if request.method == 'POST':
        legajo = request.form['legajo']
        digitos = request.form['dig']
        dependencia = request.form['dependencia']
        xfecha = date.today()
        trabajador = Trabajador.query.filter_by(legajo = legajo).first()
        if not trabajador:
            return render_template ('error.html', mensaje = 'No se encontró el trabajador ingresado.')
        if trabajador.dni[-4:] != digitos:
            return render_template ('error.html', mensaje = f'El DNI proporcionado no coincide con el de {trabajador.apellido} {trabajador.nombre}.')
        entradaExiste = RegistroHorario.query.filter_by(idtrabajador = trabajador.id, fecha = xfecha).first()
        if entradaExiste:
            return render_template ('aviso.html', mensaje = f'El trabajador {trabajador.apellido} {trabajador.nombre} ya ha ingresado hoy, {xfecha} .')
        entradaNueva = RegistroHorario(
            idtrabajador = trabajador.id,
            fecha = xfecha,
            horaentrada = datetime.now().time(),
            dependencia = dependencia)
        db.session.add(entradaNueva)
        db.session.commit()
        return render_template ('aviso.html', mensaje = f'Registro de entrada exitoso para {trabajador.apellido} {trabajador.nombre}.')
    return render_template('RegistraEntrada.html')

@app.route('/RegistraSalida', methods = ['GET', 'POST'])
def RegistraSalida():
    if request.method == 'POST':
        legajo = request.form['legajo']
        digitos = request.form['dig']
        xfecha = date.today()
        trabajador = Trabajador.query.filter_by(legajo = legajo).first()
        if not trabajador:
            return render_template ('aviso.html', mensaje = 'No se encontró el trabajador ingresado.')
        if trabajador.dni[-4:] != digitos:
            return render_template ('aviso.html', mensaje = f'El DNI proporcionado no coincide con el de {trabajador.apellido} {trabajador.nombre}.')
        entradaExiste = RegistroHorario.query.filter_by(idtrabajador = trabajador.id, fecha = xfecha).first()
        if entradaExiste:
            if not entradaExiste.horasalida:
                xhora = datetime.now().time()
                entradaExiste.horasalida = xhora
                xdepe = entradaExiste.dependencia
                if xdepe == 'D01':
                    xdepe = 'Edificio Central'
                elif xdepe == 'D02':
                    xdepe = 'Talleres'
                elif xdepe == 'D03':
                    xdepe = 'Centro deportivo'
                db.session.commit()
                return render_template ('aviso.html', mensaje = f'Registro de salida exitoso, Nombre: {trabajador.apellido} {trabajador.nombre} Dependencia: {xdepe}.')
            else:
                return render_template ('aviso.html', mensaje = f'Hoy {xfecha} {trabajador.apellido} {trabajador.nombre} ya se ha retirado.')
        else:
            return render_template ('aviso.html', mensaje = f'Hoy {xfecha} El trabajador/a {trabajador.apellido} {trabajador.nombre} no ingresó.')
    return render_template('RegistraSalida.html')

@app.route('/ConsultarRegistro', methods = ['GET', 'POST'])
def ConsultarRegistro():
    if request.method == 'POST':
        legajo = request.form['legajo']
        digitos = request.form['dig']
        fechaI = request.form['fechaI']
        fechaF = request.form['fechaF']
        trabajador = Trabajador.query.filter_by(legajo = legajo).first()
        if not trabajador:
            return render_template ('aviso.html', mensaje = 'No se encontró el trabajador ingresado.')
        if trabajador.dni[-4:] == digitos:
            xregs = RegistroHorario.query.filter(
                RegistroHorario.idtrabajador == trabajador.id,
                RegistroHorario.fecha >= fechaI,
                RegistroHorario.fecha <= fechaF
            ).order_by(RegistroHorario.fecha).all()
            if xregs:
                xnombre = trabajador.apellido + ' ' + trabajador.nombre
                return render_template('Mostrador.html', registros = xregs, nombre = xnombre)
            else:
                return render_template ('aviso.html', mensaje = f'{trabajador.apellido} {trabajador.nombre} no posee registros en el período ingresado.')
        else:
            return render_template ('aviso.html', mensaje = f'El DNI proporcionado no coincide con el de {trabajador.apellido} {trabajador.nombre}.')
    return render_template('/ConsultarRegistro.html')


if __name__ == '__main__':
    app.run(debug = True)
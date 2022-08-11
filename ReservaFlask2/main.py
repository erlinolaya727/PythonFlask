import database as bd
from sqlite3 import Error, dbapi2
import sqlite3
from flask import Flask, flash, render_template,request,session,url_for
from markupsafe import escape
from requests import RequestException
from werkzeug.utils import redirect
from datetime import datetime
import uuid


app=Flask(__name__)

app.secret_key='Mi_llave_secreta'


@app.route('/')
def inicio():
    if 'username' in session:
        return redirect(url_for('Reserva'))
    return 'No ha hecho login'

    # app.logger.info(f'Entramos al path {request.path}')
    # return "Hola mundo desde flask"
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Omitimos validacion de usuario y password
        usuario = request.form['username']
        # agregar el usuario a la session
        session['username'] = usuario
        #session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout',methods=['POST','GET'])
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/habitaciones')
def Reserva():    
    return render_template("shop.html")

@app.route('/asignarHabitacion/<int:nHab>',methods=['GET','POST'])
def AsignarHabitacion(nHab):
    conn = sqlite3.connect("hoteldb.db")
    cursor = conn.cursor()
    instruction = f"SELECT check_out_date FROM reserva WHERE room_booking = '{nHab}'ORDER BY id DESC;"
    cursor.execute(instruction)
    fmin = cursor.fetchone()
    conn.commit()
    conn.close()
    if fmin ==None:
        fmin = datetime.now()
        fmin = fmin.strftime("%Y-%m-%d")
    else:
        fmin = fmin[0]
    print(fmin)
    usuario = session['username']
    return render_template("shop-single.html",nHab=nHab,usuario=usuario,fmin=fmin)

@app.route('/VerReserva')
def ver_reserva():
    usuario = session['username']
    conn = sqlite3.connect("hoteldb.db")
    cursor = conn.cursor()
    instruction = f"SELECT id FROM user WHERE email_address = '{usuario}'"
    cursor.execute(instruction)
    id = cursor.fetchone()
    conn.commit()
    conn.close()
    id=int(id[0])
    print(id)

    conn = sqlite3.connect("hoteldb.db")
    cursor = conn.cursor()
    instruction2 = f"SELECT room_booking,check_in_date,check_out_date,costo_reserva FROM reserva WHERE user_booking = {id} ORDER BY id DESC;"
    cursor.execute(instruction2)
    reserva = cursor.fetchone()
    conn.commit()
    conn.close()
    hab=reserva[0]
    fecha_ingreso=reserva[1]
    fecha_salida=reserva[2]
    costo = reserva[3]
    
    return render_template("Avisoreserva.html",hab=hab,fecha_ingreso=fecha_ingreso,fecha_salida=fecha_salida,costo=costo,usuario=usuario)

    
@app.route('/rHab/<int:nHab>',methods=['GET','POST'])
def reservaHabitacion(nHab):
    usuario = session['username']
    conn = sqlite3.connect("hoteldb.db")
    cursor = conn.cursor()
    instruction = f"SELECT id FROM user WHERE email_address = '{usuario}'"
    cursor.execute(instruction)
    Ide = cursor.fetchone()
    conn.commit()
    conn.close()
    Ide=int(Ide[0])

    if request.method == 'POST':
        NumeroHab = nHab
        fecha_ingreso = request.form['fecha_ingreso']
        fecha_salida = request.form['fecha_egreso']
        num_reserva = str(uuid.uuid4().int)
        date1=datetime.strptime(fecha_ingreso, '%Y-%m-%d')
        date2=datetime.strptime(fecha_salida, '%Y-%m-%d')
        dif= date2-date1
        dif=dif.days
        precio = (dif*100000)
        if dif>0:
            bd.sql_insert_reserva(num_reserva,fecha_ingreso,fecha_salida,precio,NumeroHab,Ide)
            return redirect(url_for("ver_reserva"))
        else:
            return redirect(url_for("Reserva"))
app.run(debug=True)
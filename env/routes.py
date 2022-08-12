from env import app
from flask import render_template, request, flash, redirect, url_for
from env.models import User, Room, Reserva
from env import db
from datetime import datetime
#from sqlite3 import Error, dbapi2
import sqlite3
import uuid

'''
Reservar Habitaciones - Jorge
'''

@app.route('/habitaciones')
def Reservar():    
    return render_template("shop.html")

@app.route('/asignarHabitacion/<int:nHab>',methods=['GET','POST'])
def AsignarHabitacion(nHab):
    
    conn = sqlite3.connect('./env/db/hoteldb.db')
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
    usuario = User.query.filter_by(email_address='vicentefb@uninorte.edu.co').first().email_address
    return render_template("shop-single.html",nHab=nHab,usuario=usuario,fmin=fmin)

@app.route('/VerReserva')
def ver_reserva():
    usuario = User.query.filter_by(email_address='vicentefb@uninorte.edu.co').first().email_address
    conn = sqlite3.connect("./env/db/hoteldb.db")
    cursor = conn.cursor()
    instruction = f"SELECT id FROM user WHERE email_address = '{usuario}'"
    cursor.execute(instruction)
    id = cursor.fetchone()
    conn.commit()
    conn.close()
    id=int(id[0])
    print(id)

    conn = sqlite3.connect("./env/db/hoteldb.db")
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
    usuario = User.query.filter_by(email_address='vicentefb@uninorte.edu.co').first().email_address
    conn = sqlite3.connect("./env/db/hoteldb.db")
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
        #num_reserva = str(uuid.uuid4().int)
        date1=datetime.strptime(fecha_ingreso, '%Y-%m-%d')
        date2=datetime.strptime(fecha_salida, '%Y-%m-%d')
        #dif= (date2-date1).days
        #dif=dif.days
        #precio = (dif*100000)
        
        if (date2-date1).days > 0:
            Reserva.create_reserva(date1, date2,NumeroHab,Ide)
            return redirect(url_for("ver_reserva"))
            
        else:
            
            return redirect(url_for("Reserva"))

'''
Panel SuperUsuario - Vicente
'''

@app.route('/controlpanel')
def home_page():
    return render_template('panelSuper.html')

@app.route('/control_user', methods=['GET','POST'])
def crud_usuario_page():
    
    if request.method == 'POST':        
        updated_user = User.query.filter_by(id=request.form.get('id')).first()        
        if request.form.get('action') == 'editar':            
            updated_user.name = request.form.get('name')
            updated_user.birth_date = datetime.strptime(str(request.form.get('nacimiento')),'%Y-%m-%d')
            updated_user.rol = request.form.get('rol')
            updated_user.phone = request.form.get('phone')
            updated_user.document = request.form.get('documento')
            updated_user.email = request.form.get('email')
            db.session.add(updated_user)
            db.session.commit()            
            flash('Usuario actualizado',category='success')        
        if request.form.get('action') == 'agregar':            
            User.create_user(request.form.get('name'),datetime.strptime(str(request.form.get('nacimiento')),'%Y-%m-%d'),request.form.get('rol'),request.form.get('phone'),
                             request.form.get('documento'),request.form.get('email'),'password_temp')            
            flash('Usuario Creado',category='success')             
        if request.form.get('action') == 'eliminar':            
            User.delete_user(updated_user.id)
            flash('Usuario eliminado',category='success')          
        return redirect(url_for('crud_usuario_page'))
    if request.method == 'GET':        
        users = User.query.all()
        return render_template('userCrud.html',users = users)

@app.route('/control_rooms', methods=['GET','POST'])
def crud_room_page():
    
    if request.method == 'POST':
        
        updated_room = Room.query.filter_by(id=request.form.get('id')).first()
        
        if request.form.get('action') == 'editar':
            
            try:
                
                updated_room.roomNumber = request.form.get('name')
                updated_room.disponibilidad = request.form.get('disponibilidad')
                     
                db.session.add(updated_room)
                db.session.commit()
            
                flash('Habitacion actualizada con exito',category='success')
                
            except:
                
                flash('Revise informacion suministrada',category='danger')
        
        if request.form.get('action') == 'agregar':
            
            try:  
                Room.create_room(request.form.get('room_number'), int(request.form.get('disponibilidad')))
                flash('Habitacion creada con exito',category='success') 
            except:
                flash('Revise informacion suministrada',category='danger')
        
        if request.form.get('action') == 'eliminar':
            
            Room.delete_room(id=updated_room.id)
            flash('Habitacion eliminada', category='success') 
            
        return redirect(url_for('crud_room_page'))
        
    if request.method == 'GET':
        
        rooms = Room.query.all()
        return render_template('roomCrud.html',rooms = rooms)

@app.route('/control_reservation', methods=['GET','POST'])
def crud_reservation_page():
    
    if request.method == 'POST':
        
        updated_reserva = Reserva.query.filter_by(id=request.form.get('id')).first()
               
        if request.form.get('action') == 'eliminar':
            
            try:
                
                Reserva.delete_reserva(id=updated_reserva.id)
                flash('Habitacion eliminada', category='success')
            
            except:
                              
                flash('Revise informacion suministrada', category='danger')
                
        return redirect(url_for('crud_reservation_page'))
                          
    if request.method == 'GET':
    
        reservations = Reserva.query.all()
        return render_template('reservationCrud.html', reservations=reservations)

'''
Panel Administrador - Erlin
'''

@app.route('/Administrador')
def adminPage():
    return render_template('Administrador.html')

@app.route('/control_user_admin', methods=['GET','POST'])
def crud_usuario_admin():
    
    if request.method == 'POST':        
        updated_user = User.query.filter_by(id=request.form.get('id')).first()        
        if request.form.get('action') == 'editar':            
            updated_user.name = request.form.get('name')
            updated_user.birth_date = datetime.strptime(str(request.form.get('nacimiento')),'%Y-%m-%d')
            updated_user.rol = request.form.get('rol')
            updated_user.phone = request.form.get('phone')
            updated_user.document = request.form.get('documento')
            updated_user.email = request.form.get('email')
            db.session.add(updated_user)
            db.session.commit()            
            flash('Usuario actualizado',category='success')        
        if request.form.get('action') == 'agregar':            
            User.create_user(request.form.get('name'),datetime.strptime(str(request.form.get('nacimiento')),'%Y-%m-%d'),request.form.get('rol'),request.form.get('phone'),
                             request.form.get('documento'),request.form.get('email'),'password_temp')            
            flash('Usuario Creado',category='success')             
        if request.form.get('action') == 'eliminar':            
            User.delete_user(updated_user.id)
            flash('Usuario eliminado',category='success')          
        return redirect(url_for('crud_usuario_admin'))    
    if request.method == 'GET':        
        users = User.query.all()
        return render_template('userCrudAdmin.html',users = users)

@app.route('/control_rooms_admin', methods=['GET','POST'])
def crud_room_admin():
    
    if request.method == 'POST':        
        updated_room = Room.query.filter_by(id=request.form.get('id')).first()        
        if request.form.get('action') == 'editar':            
            try:                
                updated_room.roomNumber = request.form.get('name')
                updated_room.disponibilidad = request.form.get('disponibilidad')                     
                db.session.add(updated_room)
                db.session.commit()            
                flash('Habitacion actualizada con exito',category='success')                
            except:                
                flash('Revise informacion suministrada',category='danger')        
        if request.form.get('action') == 'agregar':            
            try:  
                Room.create_room(request.form.get('room_number'), int(request.form.get('disponibilidad')))
                flash('Habitacion creada con exito',category='success') 
            except:
                flash('Revise informacion suministrada',category='danger')        
        if request.form.get('action') == 'eliminar':            
            Room.delete_room(id=updated_room.id)
            flash('Habitacion eliminada', category='success')             
        return redirect(url_for('crud_room_admin'))        
    if request.method == 'GET':        
        rooms = Room.query.all()
        return render_template('roomCrudAdmin.html',rooms = rooms)

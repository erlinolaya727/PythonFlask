from env import app
from flask import render_template, request, flash, redirect, url_for
from env.models import User, Room, Reserva
from env import db
from datetime import datetime

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
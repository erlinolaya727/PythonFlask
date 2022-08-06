from env import app
from flask import render_template, request, flash, redirect, url_for
from env.models import User, Room
from env import db

@app.route('/controlpanel')
def home_page():
    return render_template('panelSuper.html')

@app.route('/control_user', methods=['GET','POST'])
def crud_usuario_page():
    
    if request.method == 'POST':
        
        updated_user = User.query.filter_by(id=request.form.get('id')).first()
        
        updated_user.name = request.form.get('name')
        updated_user.rol = request.form.get('rol')
        
        db.session.add(updated_user)
        db.session.commit()

        flash('Usuario actualizado',category='success')
        
        return redirect(url_for('crud_usuario_page'))

    if request.method == 'GET':
        
        users = User.query.all()
        return render_template('userCrud.html',users = users)

@app.route('/control_rooms')
def crud_room_page():
    rooms = Room.query.all()
    return render_template('roomCrud.html',rooms = rooms)

@app.route('/control_reservation')
def crud_reservation_page():
    rooms = Room.query.all()
    return render_template('reservationCrud.html')
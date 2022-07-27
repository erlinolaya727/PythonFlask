from env import app
from flask import render_template
from env.models import User, Room

@app.route('/controlpanel')
def home_page():
    return render_template('panelSuper.html')

@app.route('/control_user')
def crud_usuario_page():
    users = User.get_objects()
    return render_template('userCrud.html',users = users)

@app.route('/control_rooms')
def crud_room_page():
    rooms = Room.get_objects()
    return render_template('roomCrud.html',rooms = rooms)
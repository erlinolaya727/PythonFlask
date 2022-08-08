from env import db
from env.models import User, Room, Calificacion, Reserva, delete_record
from datetime import datetime, timedelta

'''
Borrar toda la Base de datos
'''

db.drop_all()

'''
Crear la BD y sus tablas
'''

db.create_all()

'''
Instanciar las diferentes tablas, codigo sirve para demostrar como se crean nuevos registros en la db
'''

User.create_user('Vicente F', '05/16/1992','Administrador',5555555555,123456789,'vicentefb@uninorte.edu.co','password')
User.create_user('Juan P', '05/16/1992','Administrador',5555555556,123456788,'juanpf@uninorte.edu.co','password')
User.create_user('Juan B', '05/16/1992','Usuario',5555555546,123456388,'juanbr@uninorte.edu.co','password')
User.create_user('Valentina O', '05/16/1992','Usuario',5555555356,123496788,'valentinaop@uninorte.edu.co','password')
User.create_user('Daniela A', '05/16/1992','Administrador',5555535356,129496788,'danielaa@uninorte.edu.co','password')
Room.create_room('101', 0)
Room.create_room('201', 1)
Room.create_room('301', 1)
Room.create_room('401', 0)
Room.create_room('102', 0)
Calificacion.create_score(2,'Sabanas sucias')
Calificacion.create_score(3,'Buena atención')
Calificacion.create_score(4,'Buen desayuno')
Calificacion.create_score(5,'Excelente atención')
Calificacion.create_score(1,'Ratas en el baño')

Reserva.create_reserva(str(datetime.now()),str(datetime.now() + timedelta(days=2)),5,5,1)
Reserva.create_reserva(str(datetime.now()),str(datetime.now() + timedelta(days=2)),4,4,2)
Reserva.create_reserva(str(datetime.now()),str(datetime.now() + timedelta(days=2)),3,3,3)
Reserva.create_reserva(str(datetime.now()),str(datetime.now() + timedelta(days=2)),2,2,4)
Reserva.create_reserva(str(datetime.now()),str(datetime.now() + timedelta(days=2)),1,1,2)

'''
Queries & Assignations
'''

#print(User.query.all())
#print(Room.query.all())
#print(Calificacion.query.all())


'''
Asignaciones Usuario - Habitaciones - Comentarios
'''
score_1 = Calificacion.query.filter_by(num_score=3).first()
score_1.room_commented = Room.query.filter_by(roomNumber = '102').first().id # Grabs the first id of the filtered roomnumber and asign it to the score of the room with score of 3
db.session.add(score_1)
db.session.commit()
print(score_1.room_commented)
score_1.commented_by = User.query.filter_by(name='Vicente F').first().id
db.session.add(score_1)
db.session.commit()
print(score_1.commented_by)

'''
Asignacion Usuario - Habiatcion - Reserva
Con este codigo puedo acceder a cualquier informacion de otras tablas usando "back-ref" que se
define al crear la referencia en models.py Puedo acceder tanto a usuario como a habitacion debido a la definicion
'''
print(Reserva.query.filter_by(id=2).first().booked_by)
print(Reserva.query.filter_by(id=2).first().room_booked)

Reserva.delete_reserva(3)

'''
Pequeño metodo para borrar registros transversales,
porfavor usar si se quiere usar para borrar entradas en todas las tablas (de requerirse) se puede personalizar,
utilziar com base
'''
#delete_record(id=3)

#print(Calificacion.query.filter_by(num_score=3).first().commented_by)
#i = Calificacion.query.filter_by(num_score = 3).first()
#print(i)
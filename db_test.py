from env import db
from env.models import User, Room, Calificacion

#db.drop_all()
#db.create_all()
#User.create_user('Vicente F', '05/16/1992','Administrador',5555555555,123456789,'vicentefb@uninorte.edu.co','password')
#User.create_user('Juan P', '05/16/1992','Administrador',5555555556,123456788,'juanpf@uninorte.edu.co','password')
#User.create_user('Juan B', '05/16/1992','Usuario',5555555546,123456388,'juanbr@uninorte.edu.co','password')
#User.create_user('Valentina O', '05/16/1992','Usuario',5555555356,123496788,'valentinaop@uninorte.edu.co','password')
#User.create_user('Daniela A', '05/16/1992','Administrador',5555535356,129496788,'danielaa@uninorte.edu.co','password')
#Room.create_room('101', 0)
#Room.create_room('201', 1)
#Room.create_room('301', 1)
#Room.create_room('401', 0)
#Room.create_room('102', 0)
#Calificacion.create_score(2,'Sabanas sucias')
#Calificacion.create_score(3,'Buena atención')
#Calificacion.create_score(4,'Buen desayuno')
#Calificacion.create_score(5,'Excelente atención')
#Calificacion.create_score(1,'Ratas en el baño')

'''
Queries & Assignations
'''

#print(User.query.all())
#print(Room.query.all())
#print(Calificacion.query.all())

#score_1 =Calificacion.query.filter_by(num_score=3).first()
#score_1.room_commented = Room.query.filter_by(roomNumber = '102').first().id # Grabs the first id of the filtered roomnumber and asign it to the score of the room with score of 3
#db.session.add(score_1)
#db.session.commit()
#print(score_1.room_commented)
#score_1.commented_by = User.query.filter_by(name='Vicente F').first().id
#db.session.add(score_1)
#db.session.commit()
#print(score_1.commented_by)

#print(Calificacion.query.filter_by(num_score=3).first().commented_by)
#i = Calificacion.query.filter_by(num_score = 3).first()
#print(i)
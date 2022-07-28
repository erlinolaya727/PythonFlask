from env import db
from env.models import User, Room

db.create_all()

#User.create_user('Vicente F', 'vicentefb','administrador',5555555555,123456789,'vicentefb@uninorte.edu.co','password')
#User.create_user('Juan P', 'juanpf','administrador',5555555556,123456788,'juanpf@uninorte.edu.co','password')
#User.create_user('Juan B', 'juanbr','usuario',5555555546,123456388,'juanbr@uninorte.edu.co','password')
#User.create_user('Valentina O', 'valentinaop','usuario',5555555356,123496788,'valentinaop@uninorte.edu.co','password')
#User.create_user('Daniela A', 'danielaa','administrador',5555535356,129496788,'danielaa@uninorte.edu.co','password')
#User.get_objects()

#Room.create_room(101,2,'No Disponible')
#Room.create_room(201,2,'Disponible')
#Room.create_room(301,2,'Disponible')
#Room.create_room(401,2,'No Disponible')
#Room.create_room(102,2,'No Disponible')
#print(Room.get_objects())
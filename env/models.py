from datetime import date
from env import db
from env import func

user_room = db.Table('user_room',
                     db.Column('user_id', db.Integer,
                               db.ForeignKey('user.id')),
                     db.Column('room_id', db.Integer, db.ForeignKey('room.id'))
                     )


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=45), nullable=False)
    birth_date = db.Column(db.String(length=10), nullable=False)
    rol = db.Column(db.String(length=20), nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    document = db.Column(db.Integer, nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),
                              nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    comments = db.relationship(
        'Calificacion', backref='comment_by', lazy=True)

    def __init__(self, name: str, birth_date: date, rol: str, phone: int, document: int, email_address: str, password_hash: str):

        self.name = name
        self.birth_date = birth_date
        self.rol = rol
        self.phone = phone
        self.document = document
        self.email_address = email_address
        self.password_hash = password_hash

    def __repr__(self):
        return f'User: {self.name} \n'

    def create_user(name: str, birth_date: date, rol: str, phone: int, document: int, email_address: str, password_hash: str):
        user = User(name, birth_date, rol, phone,
                    document, email_address, password_hash)

        db.session.add(user)
        db.session.commit()
        db.session.close()


class Room(db.Model):

    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roomNumber = db.Column(db.String(length=3), nullable=False, unique=True)
    disponibilidad = db.Column(db.Integer, nullable=False)

    calificacion = db.relationship(
        'Calificacion', backref='room_score', lazy=True)

    #created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())
    #host = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, roomNumber: int, disponibilidad: int):

        self.roomNumber = roomNumber
        self.disponibilidad = disponibilidad

    def create_room(roomNumber: int, disponibilidad: int):
        room = Room(roomNumber, disponibilidad)
        db.session.add(room)
        db.session.commit()
        db.session.close()

    def __repr__(self):
        return f'Habitacion No.: {self.roomNumber} - Estado: {self.disponibilidad} \n'


class Calificacion(db.Model):

    __tablename__ = 'score'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_score = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(length=150), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    room_commented = db.Column(db.Integer, db.ForeignKey('room.id'))
    commented_by = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, num_score: int, comentario: str):
        self.num_score = num_score
        self.comentario = comentario

    def create_score(num_score: int, comentario: str):
        score = Calificacion(num_score, comentario)
        db.session.add(score)
        db.session.commit()
        db.session.close()

    def __repr__(self):
        return f'Calificacion: {self.num_score} - Comentario: {self.comentario} \n'

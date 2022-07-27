from env import db
from env import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    attribute = db.Column(db.String(length=15), nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    document = db.Column(db.Integer, nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())
    room = db.relationship('Room',backref='room_asigned', lazy=True)
    
    def __init__(self, name:str, username: str, attribute:str,phone: int, document:int,email_address: str, password_hash: str):
        
        self.name = name
        self.username = username
        self.attribute = attribute
        self.phone = phone
        self.document = document
        self.email_address= email_address
        self.password_hash = password_hash
        
    def __repr__(self):
        return f'User {self.username}'
        
    def create_user(name:str, username: str, attribute:str, phone: int, document:int,email_address: str, password_hash: str):
        user = User(name,username,attribute,phone,document,email_address,password_hash)
        db.session.add(user)
        db.session.commit()
    
    def get_objects():
        return User.query.all()
    
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    roomNumber = db.Column(db.Integer, nullable=False, unique=True)
    size = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(length=15), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())
    host = db.Column(db.String(length=30), db.ForeignKey('user.id'))
    
    
    def __init__(self, roomNumber:int, size:int, state:str):
        
        self.roomNumber = roomNumber
        self.size = size
        self.state = state
        
    def create_room(roomNumber:int, size:int,state:str):
        room = Room(roomNumber, size, state)
        db.session.add(room)
        db.session.commit()
    
    def __repr__(self):
        return f'Room: {self.roomNumber}'
    
    def get_objects():
        return Room.query.all()
    

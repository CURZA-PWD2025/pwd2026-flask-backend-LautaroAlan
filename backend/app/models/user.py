from app.models import db
from app.models.base_model import BaseModel 
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel): 
    __tablename__ = 'users'
    
    nombre = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(200), unique=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password = db.Column(db.String(255))
    
    rol = db.relationship('Rol', back_populates='users')

    def __init__(self, nombre:str, email:str, password:str, rol_id:int = 1) -> None:
        self.nombre = nombre
        self.email = email
        self.rol_id = rol_id
        self.generate_password(password)
    
    def __repr__(self):
        return f"usuario {self.nombre}, email {self.email}, fecha de creacion {self.created_at}" 
     
    def to_dict(self, include_rol=True): 
        data = super().to_dict()
        
        data.update({
            'nombre': self.nombre,
            'email': self.email,
            'rol_id': self.rol_id
        })
        
        if include_rol and self.rol:
            data['rol'] = self.rol.to_dict(include_users=False)
            
        return data
      
    def validate_password(self, password:str) -> bool:
        return check_password_hash(self.password, password)
    
    def generate_password(self, password:str):
        self.password = generate_password_hash(password)
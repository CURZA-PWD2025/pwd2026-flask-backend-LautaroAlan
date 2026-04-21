# app/models/rol.py
from app.models import db
from app.models.base_model import BaseModel

class Rol(BaseModel):
    __tablename__ = "roles"
    
  
    nombre = db.Column(db.String, unique=True, nullable=False)
    users = db.relationship('User', back_populates='rol')
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def to_dict(self, include_users=True):
        data = super().to_dict()
        data.update({
            'nombre': self.nombre
        })
        
        if include_users and self.users:
            data['users'] = [user.to_dict(include_rol=False) for user in self.users]
            
        return data
from app.models import db
from app.models.base_model import BaseModel

class Proveedor(BaseModel):
    __tablename__ = 'proveedores'

    nombre = db.Column(db.String(150), unique=True, nullable=False)
    contacto = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(120), nullable=True)

    productos = db.relationship('Producto', back_populates='proveedor')

    def __init__(self, nombre: str, contacto: str = None, telefono: str = None, email: str = None):
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono  
        self.email = email        

  
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'nombre': self.nombre,
            'contacto': self.contacto,
            'telefono': self.telefono, 
            'email': self.email        
        })
        return data
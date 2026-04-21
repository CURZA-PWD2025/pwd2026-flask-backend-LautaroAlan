from app.models import db
from app.models.base_model import BaseModel

class Categoria(BaseModel):
    __tablename__ = 'categorias'

    nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)

    productos = db.relationship('Producto', back_populates='categoria')

    def __init__(self, nombre: str, descripcion: str = None):
        self.nombre = nombre
        self.descripcion = descripcion

    def to_dict(self, include_productos=False):
        data = super().to_dict()
        
        data.update({
            'nombre': self.nombre,
            'descripcion': self.descripcion
        })
        
        if include_productos and self.productos:
            data['productos'] = [p.to_dict() for p in self.productos]
            
        return data
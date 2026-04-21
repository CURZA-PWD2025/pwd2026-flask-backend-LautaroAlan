from app.models import db
from app.models.base_model import BaseModel

class MovimientoStock(BaseModel):
    __tablename__ = 'movimientos_stock'

    tipo = db.Column(db.String(10), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.String(200), nullable=True)
    
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    producto = db.relationship('Producto', back_populates='movimientos')
    usuario = db.relationship('User', backref='mis_movimientos')

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo': self.tipo,
            'cantidad': self.cantidad,
            'motivo': self.motivo,
            'producto_id': self.producto_id,
            'user_id': self.user_id,
            'nombre_producto': self.producto.nombre if self.producto else None
        })
        return data
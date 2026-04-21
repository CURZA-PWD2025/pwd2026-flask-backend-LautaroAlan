from app.models import db
from app.models.base_model import BaseModel

class Producto(BaseModel):
    __tablename__ = 'productos'

    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.String(255))
    precio_costo = db.Column(db.Float, default=0.0)
    precio_venta = db.Column(db.Float, default=0.0)
    stock_actual = db.Column(db.Integer, default=0)
    stock_minimo = db.Column(db.Integer, default=0)

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)

    categoria = db.relationship('Categoria', backref='categoria_productos', overlaps="productos")
    proveedor = db.relationship('Proveedor', backref='proveedor_productos', overlaps="productos")
    movimientos = db.relationship('MovimientoStock', back_populates='producto')

    def __init__(self, nombre, categoria_id, proveedor_id, precio_costo=0.0, precio_venta=0.0, stock_actual=0, stock_minimo=0, descripcion=None):
        self.nombre = nombre
        self.categoria_id = categoria_id
        self.proveedor_id = proveedor_id
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.descripcion = descripcion
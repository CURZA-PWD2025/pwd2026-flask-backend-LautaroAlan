from app.models import db
from app.models.producto import Producto
from flask import jsonify

class ProductoController:
    @staticmethod
    def get_all():
        productos = db.session.execute(db.select(Producto)).scalars().all()
        return jsonify([p.to_dict() for p in productos]), 200

    @staticmethod
    def get_by_id(id):
        producto = db.session.query(Producto).filter(Producto.id == id).first()
        
        if not producto:
            return jsonify({'msg': f'El producto con ID {id} no existe en la base de datos'}), 404
        
        return jsonify(producto.to_dict()), 200

    @staticmethod
    def create(data):
        if not data.get('nombre'):
            return jsonify({'msg': 'El nombre es obligatorio'}), 400
        
        nuevo_prod = Producto(
            nombre=data.get('nombre'),
            categoria_id=data.get('categoria_id'),
            proveedor_id=data.get('proveedor_id'),
            precio_costo=data.get('precio_costo', 0.0),
            precio_venta=data.get('precio_venta', 0.0),
            stock_actual=data.get('stock_actual', 0),
            stock_minimo=data.get('stock_minimo', 0),
            descripcion=data.get('descripcion')
        )
        db.session.add(nuevo_prod)
        db.session.commit()
        return jsonify(nuevo_prod.to_dict()), 201

    @staticmethod
    def update(id, data):
        producto = db.session.query(Producto).filter(Producto.id == id).first()
        if not producto:
            return jsonify({'msg': 'Producto no encontrado'}), 404
        
        producto.nombre = data.get('nombre', producto.nombre)
        producto.precio_costo = data.get('precio_costo', producto.precio_costo)
        producto.precio_venta = data.get('precio_venta', producto.precio_venta)
        producto.stock_actual = data.get('stock_actual', producto.stock_actual)
        producto.stock_minimo = data.get('stock_minimo', producto.stock_minimo)
        producto.categoria_id = data.get('categoria_id', producto.categoria_id)
        producto.proveedor_id = data.get('proveedor_id', producto.proveedor_id)
        
        db.session.commit()
        return jsonify(producto.to_dict()), 200

    @staticmethod
    def delete(id):
        producto = db.session.query(Producto).filter(Producto.id == id).first()
        if not producto:
            return jsonify({'msg': 'Producto no encontrado'}), 404
        db.session.delete(producto)
        db.session.commit()
        return jsonify({'msg': 'Producto eliminado'}), 200
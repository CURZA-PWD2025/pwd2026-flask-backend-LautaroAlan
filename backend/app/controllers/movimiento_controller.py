from app.models import db, MovimientoStock, Producto
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

class MovimientoController:
    @staticmethod
    def create(data):
        producto = db.session.get(Producto, data.get('producto_id'))
        if not producto:
            return jsonify({'error': 'Producto no encontrado'}), 404

        cantidad = int(data.get('cantidad', 0))
        if cantidad <= 0:
            return jsonify({'error': 'La cantidad debe ser mayor a 0'}), 400

        tipo = data.get('tipo').lower()
        user_id = get_jwt_identity()

        if tipo == 'entrada':
            producto.stock_actual += cantidad
        elif tipo == 'salida':
            if producto.stock_actual < cantidad:
                return jsonify({'error': f'Stock insuficiente. Disponible: {producto.stock_actual}'}), 400
            producto.stock_actual -= cantidad
        else:
            return jsonify({'error': "El tipo debe ser 'entrada' o 'salida'"}), 400

        nuevo_mov = MovimientoStock(
            tipo=tipo,
            cantidad=cantidad,
            motivo=data.get('motivo'),
            producto_id=producto.id,
            user_id=user_id
        )

        try:
            db.session.add(nuevo_mov)
            db.session.commit()
            return jsonify(nuevo_mov.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
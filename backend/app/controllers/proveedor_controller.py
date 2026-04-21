from app.models import db
from app.models.proveedor import Proveedor
from flask import jsonify

class ProveedorController:
    @staticmethod
    def get_all():
        proveedores = db.session.execute(db.select(Proveedor)).scalars().all()
        return jsonify([p.to_dict() for p in proveedores]), 200

    @staticmethod
    def get_by_id(id):
        proveedor = db.session.get(Proveedor, id)
        if not proveedor:
            return jsonify({'msg': 'Proveedor no encontrado'}), 404
        return jsonify(proveedor.to_dict()), 200

    @staticmethod
    def create(data):
        if not data.get('nombre'):
            return jsonify({'msg': 'El nombre es obligatorio'}), 400
        
        nuevo_prov = Proveedor(
            nombre=data.get('nombre'),
            contacto=data.get('contacto'),
            telefono=data.get('telefono'),
            email=data.get('email')
        )
        db.session.add(nuevo_prov)
        db.session.commit()
        return jsonify(nuevo_prov.to_dict()), 201

    @staticmethod
    def update(id, data):
        proveedor = db.session.get(Proveedor, id)
        if not proveedor:
            return jsonify({'msg': 'Proveedor no encontrado'}), 404
        
        proveedor.nombre = data.get('nombre', proveedor.nombre)
        proveedor.contacto = data.get('contacto', proveedor.contacto)
        proveedor.telefono = data.get('telefono', proveedor.telefono)
        proveedor.email = data.get('email', proveedor.email)
        
        db.session.commit()
        return jsonify(proveedor.to_dict()), 200

    @staticmethod
    def delete(id):
        proveedor = db.session.get(Proveedor, id)
        if not proveedor:
            return jsonify({'msg': 'Proveedor no encontrado'}), 404
        
        db.session.delete(proveedor)
        db.session.commit()
        return jsonify({'msg': 'Proveedor eliminado correctamente'}), 200
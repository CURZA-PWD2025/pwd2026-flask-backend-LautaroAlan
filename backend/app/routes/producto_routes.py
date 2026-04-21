from flask import Blueprint, request
from app.controllers.producto_controller import ProductoController
from app.decorators.rol_access import rol_access

productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@productos_bp.route('/', methods=['GET'])
@rol_access('admin', 'user') 
def get_all():
    return ProductoController.get_all()

@productos_bp.route('/<int:id>', methods=['GET'])
@rol_access('admin', 'user')
def get_by_id(id):
    return ProductoController.get_by_id(id)

@productos_bp.route('/', methods=['POST'])
@rol_access('admin') 
def create():
    return ProductoController.create(request.get_json())

@productos_bp.route('/<int:id>', methods=['PUT'])
@rol_access('admin')
def update(id):
    return ProductoController.update(id, request.get_json())

@productos_bp.route('/<int:id>', methods=['DELETE'])
@rol_access('admin')
def delete(id):
    return ProductoController.delete(id)
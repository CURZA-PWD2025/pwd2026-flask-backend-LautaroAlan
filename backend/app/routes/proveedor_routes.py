from flask import Blueprint, request
from app.controllers.proveedor_controller import ProveedorController
from app.decorators.rol_access import rol_access

proveedores_bp = Blueprint('proveedores', __name__, url_prefix='/proveedores')

@proveedores_bp.route('/', methods=['GET'])
@rol_access('admin', 'user')
def get_all():
    return ProveedorController.get_all()

@proveedores_bp.route('/<int:id>', methods=['GET'])
@rol_access('admin', 'user')
def get_by_id(id):
    return ProveedorController.get_by_id(id)

@proveedores_bp.route('/', methods=['POST'])
@rol_access('admin')
def create():
    return ProveedorController.create(request.get_json())

@proveedores_bp.route('/<int:id>', methods=['PUT'])
@rol_access('admin')
def update(id):
    return ProveedorController.update(id, request.get_json())

@proveedores_bp.route('/<int:id>', methods=['DELETE'])
@rol_access('admin')
def delete(id):
    return ProveedorController.delete(id)
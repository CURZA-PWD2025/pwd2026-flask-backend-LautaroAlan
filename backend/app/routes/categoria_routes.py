from flask import Blueprint, request
from app.controllers.categoria_controller import CategoriaController
from app.decorators.rol_access import rol_access

categorias_bp = Blueprint('categorias', __name__, url_prefix='/categorias')

@categorias_bp.route('/', methods=['GET'])
@rol_access('admin', 'user') 
def get_all():
    return CategoriaController.get_all()
@categorias_bp.route('/<int:id>', methods=['GET'])
@rol_access('admin', 'user')
def get_by_id(id):
    return CategoriaController.get_by_id(id)

@categorias_bp.route('/', methods=['POST'])
@rol_access('admin') 
def create():
    return CategoriaController.create(request.get_json())

@categorias_bp.route('/<int:id>', methods=['PUT'])
@rol_access('admin')
def update(id):
    return CategoriaController.update(id, request.get_json())

@categorias_bp.route('/<int:id>', methods=['DELETE'])
@rol_access('admin')
def delete(id):
    return CategoriaController.delete(id)
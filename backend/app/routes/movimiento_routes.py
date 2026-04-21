from flask import Blueprint, request, jsonify
from app.controllers.movimiento_controller import MovimientoController
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.decorators.rol_access import rol_access
from app.models import db, MovimientoStock

movimientos_bp = Blueprint('movimientos', __name__, url_prefix='/movimientos')

@movimientos_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    return MovimientoController.create(request.get_json())

@movimientos_bp.route('/', methods=['GET'])
@rol_access('admin')
def get_all():
    movs = db.session.execute(db.select(MovimientoStock)).scalars().all()
    return jsonify([m.to_dict() for m in movs]), 200

@movimientos_bp.route('/mis/', methods=['GET'])
@jwt_required()
def get_my_moves():
    user_id = get_jwt_identity()
    movs = db.session.execute(db.select(MovimientoStock).filter_by(user_id=user_id)).scalars().all()
    return jsonify([m.to_dict() for m in movs]), 200
from app.models import db
from app.models.user import User
from app.models.rol import Rol
from flask import Response, jsonify, request as flask_request
from flask_jwt_extended import create_access_token, get_jwt_identity
from sqlalchemy.exc import IntegrityError

class AuthController:
    @staticmethod
    def Register(request:dict) -> tuple[Response, int]:
        nombre = request.get('nombre')
        email = request.get('email')
        password = request.get('password')
        
        error = None
        if not nombre: error = 'El nombre es requerido'
        elif not email: error = 'El email es requerido'
        elif not password: error = 'La contraseña es requerida'
            
        if error is None:
            try:
                
                rol_user = db.session.execute(db.select(Rol).filter_by(nombre='user')).scalar_one_or_none()
                
                if not rol_user:
                    return jsonify({'message': "Error: El rol 'user' no existe en la base de datos"}), 500

                
                user = User(nombre=nombre, email=email, rol_id=rol_user.id, password=password)    
                
                user.generate_password(password)
                
                db.session.add(user)
                db.session.commit()
                return jsonify({'message': "usuario creado con exito"}), 201                
                
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "Usuario o email ya registrado"}), 409
        
        return jsonify ({'message': error}), 422
    
    @staticmethod
    def login(request: dict) -> tuple[Response, int]:
        email = request.get('email') 
        password = request.get('password')
        
        if not email or not password:
            return jsonify({'message': "Email y contraseña son requeridos"}), 422
            
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()
        
        if user and user.validate_password(password):
            token_claims = {'rol': user.rol.nombre if user.rol else 'user'}
            access_token = create_access_token(identity=str(user.id), additional_claims=token_claims)
            
            return jsonify({
                'access_token': access_token, 
                'rol': user.rol.nombre if user.rol else 'user', 
                'nombre': user.nombre
            }), 200
            
        return jsonify({'message': "Credenciales inválidas"}), 401
    
    @staticmethod
    def me():
        user_id = get_jwt_identity()
        user = db.session.get(User, int(user_id)) 
        
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404
            
        return jsonify({
            "id": user.id,
            "nombre": user.nombre,
            "email": user.email,
            "rol": user.rol.nombre if user.rol else "Sin rol"
        }), 200
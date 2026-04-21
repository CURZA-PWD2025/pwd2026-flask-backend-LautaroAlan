from dotenv import load_dotenv
from flask import Flask
from app.models import db
from app.config import config
from app.routes.user_routes import users
from app.routes.rol_routes import roles
from app.routes.auth_routes import auth_bp
from app.routes.categoria_routes import categorias_bp
from app.routes.proveedor_routes import proveedores_bp
from app.routes.producto_routes import productos_bp
from app.routes.movimiento_routes import movimientos_bp
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os


load_dotenv(override=True)

migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(categorias_bp, url_prefix='/categorias')
    app.register_blueprint(proveedores_bp, url_prefix='/proveedores')
    app.register_blueprint(movimientos_bp, url_prefix='/movimientos')
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(roles, url_prefix='/roles')
    
    @app.route('/')
    def home():
        return '<h1>Backend de Gestión de Stock 2026 activo<h1>'

    db.init_app(app)
    migrate.init_app(app=app, db=db)
    jwt.init_app(app)
    
    return app
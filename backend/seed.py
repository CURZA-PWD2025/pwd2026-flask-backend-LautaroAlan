from app import create_app
from app.models import db
from app.models.user import User
from app.models.rol import Rol
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.producto import Producto

app = create_app()

def seed():
    admin_role = Rol.query.filter_by(nombre='admin').first()
    user_role = Rol.query.filter_by(nombre='user').first()
    if not admin_role:
        admin_role = Rol(nombre='admin')
        db.session.add(admin_role)
    if not user_role:
        user_role = Rol(nombre='user')
        db.session.add(user_role)
    db.session.commit()

    if not User.query.filter_by(email='admin@example.com').first():
        db.session.add(User(nombre='admin', email='admin@example.com', password='admin123', rol_id=admin_role.id))
    if not User.query.filter_by(email='lauti@test.com').first():
        db.session.add(User(nombre='lauti', email='lauti@test.com', password='123', rol_id=user_role.id))
    db.session.commit()

    alm = Categoria.query.filter_by(nombre='Almacén').first()
    if not alm:
        alm = Categoria(nombre='Almacén', descripcion='Productos secos')
        db.session.add(alm)
        
    lim = Categoria.query.filter_by(nombre='Limpieza').first()
    if not lim:
        lim = Categoria(nombre='Limpieza', descripcion='Artículos de limpieza')
        db.session.add(lim)
    db.session.commit()

    prov = Proveedor.query.filter_by(nombre='Distribuidora Norte').first()
    if not prov:
        prov = Proveedor(nombre='Distribuidora Norte', telefono='2994001234')
        db.session.add(prov)
    db.session.commit()

    if not Producto.query.filter_by(nombre='Harina 000').first():
        db.session.add(Producto(
            nombre='Harina 000', precio_costo=280, precio_venta=350,
            stock_actual=50, stock_minimo=10,
            categoria_id=alm.id, proveedor_id=prov.id
        ))
        
    if not Producto.query.filter_by(nombre='Lavandina 1L').first():
        db.session.add(Producto(
            nombre='Lavandina 1L', precio_costo=150, precio_venta=210,
            stock_actual=30, stock_minimo=5,
            categoria_id=lim.id, proveedor_id=prov.id
        ))
    
    db.session.commit()
    print("✅ Seed completado con éxito (Rubro: Almacén/Limpieza).")

if __name__ == '__main__':
    with app.app_context():
        seed()
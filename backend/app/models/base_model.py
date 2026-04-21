from datetime import datetime
from app.models import db
from sqlalchemy import inspect

class BaseModel(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    activo = db.Column(db.String(1), default='S') 
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def to_dict(self):
        return {
            c.key: getattr(self, c.key) 
            for c in inspect(self).mapper.column_attrs
        }
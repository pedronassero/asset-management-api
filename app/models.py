import secrets
from app import db
from sqlalchemy.orm import relationship

class Asset(db.Model):
    __tablename__ = 'asset'
    id = db.Column(db.String(8), primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    acquisitionDate = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    status = db.Column(db.Enum('CRITICAL', 'WARNING', 'HEALTHY'), default='HEALTHY')
    nextMaintenance = db.Column(db.Date, nullable=False)
    value = db.Column(db.Float, nullable=False)
    dependencies = relationship("AssetDependency", backref="asset", cascade="all, delete-orphan")
  
    def __init__(self, userId, name, description, nextMaintenance, value, status='HEALTHY'):
        self.id = secrets.token_hex(4)
        self.userId = userId
        self.name = name
        self.description = description
        self.status = status
        self.nextMaintenance = nextMaintenance
        self.value = value


class AssetDependency(db.Model):
    __tablename__ = 'assetdependency'
    id = db.Column(db.String(8), primary_key=True)
    assetId = db.Column(db.String(8), db.ForeignKey('asset.id'))
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum('CRITICAL', 'WARNING', 'HEALTHY'), default='HEALTHY')
    nextMaintenance = db.Column(db.Date)
    value = db.Column(db.Float)

    def __init__(self, assetId, name, description, status='HEALTHY', value=None, nextMaintenance=None):
        self.id = secrets.token_hex(4)
        self.assetId = assetId
        self.name = name
        self.description = description
        self.status = status
        self.value = value    
        self.nextMaintenance = nextMaintenance
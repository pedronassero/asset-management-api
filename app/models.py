import secrets
from app import db

class Asset(db.Model):
    __tablename__ = 'asset'
    id = db.Column(db.String(8), primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    acquisitionDate = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    status = db.Column(db.Enum('CRITICAL', 'WARNING', 'HEALTHY'), default='HEALTHY')
    lifetime = db.Column(db.Text, nullable=False)

    def __init__(self, userId, name, description, status='HEALTHY', lifetime=None):
        self.id = secrets.token_hex(4)
        self.userId = userId
        self.name = name
        self.description = description
        self.status = status
        self.lifetime = lifetime

class AssetDependency(db.Model):
    __tablename__ = 'assetdependency'
    id = db.Column(db.String(8), primary_key=True)
    assetId = db.Column(db.String(8), db.ForeignKey('asset.id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    status = db.Column(db.Enum('CRITICAL', 'WARNING', 'HEALTHY'), default='HEALTHY')
    value = db.Column(db.Float)
    lifetime = db.Column(db.Text)

    def __init__(self, assetId, name, description, status='HEALTHY', value=None, lifetime=None):
        self.id = secrets.token_hex(4)
        self.assetId = assetId
        self.name = name
        self.description = description
        self.status = status
        self.value = value
        self.lifetime = lifetime    
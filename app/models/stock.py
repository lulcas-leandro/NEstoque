from app.extensions import db
from datetime import datetime, timezone

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(64), index=True, unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

class StockMovement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movement_type = db.Column(db.String(10), nullable=False)  # 'ENTRADA' ou 'SAIDA'
    quantity = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    notes = db.Column(db.Text)

    product = db.relationship('Product', backref=db.backref('movements', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('movements', lazy='dynamic'))

    def __repr__(self):
        return f'<StockMovement {self.product.name} {self.movement_type} {self.quantity}>'
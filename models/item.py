from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True) # id is a column in the table
    name = db.Column(db.String(80), unique=False, nullable=False) # name is a column in the table
    description = db.Column(db.String)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False) # price is a column in the table
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False) # store_id is a column in the table
    store = db.relationship("StoreModel", back_populates="items") # store is a column in the table
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags") # tags is a column in the table

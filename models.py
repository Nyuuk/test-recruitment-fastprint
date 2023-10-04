from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


# Model Produk
class ProductModel(db.Model):
    __tablename__ = 'products'

    id_produk = db.Column(db.Integer, primary_key=True)
    nama_produk = db.Column(db.String(100))
    harga = db.Column(db.Integer)
    kategori_id = db.Column(db.Integer, ForeignKey('categories.id_kategori'))
    status_id = db.Column(db.Integer, ForeignKey('statuses.id_status'))

    # Menambahkan relasi dengan CategoryModel dan StatusModel
    kategori = relationship('CategoryModel', foreign_keys=[kategori_id])
    status = relationship('StatusModel', foreign_keys=[status_id])

    def __init__(self, nama_produk, harga, kategori_id, status_id):
        self.nama_produk = nama_produk
        self.harga = harga
        self.kategori_id = kategori_id
        self.status_id = status_id

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"


# model Kategori
class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id_kategori = db.Column(db.Integer, primary_key=True)
    nama_kategori = db.Column(db.String(100))

    def __init__(self, nama_kategori):
        self.nama_kategori = nama_kategori

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"


# Model Status
class StatusModel(db.Model):
    __tablename__ = 'statuses'

    id_status = db.Column(db.Integer, primary_key=True)
    nama_status = db.Column(db.String(100))

    def __init__(self, nama_status):
        self.nama_status = nama_status

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"
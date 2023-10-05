from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()

class CategoryModel(Base):
    __tablename__ = 'categories'

    id_kategori = Column(Integer, autoincrement=True, primary_key=True)
    nama_kategori = Column(String)

    def __repr__(self):
        return "<CategoryModel(id_kategori='%s',nama_kategori='%s')>" % (self.id_kategori, self.nama_kategori)


class StatusModel(Base):
    __tablename__ = 'status'

    id_status = Column(Integer, autoincrement=True, primary_key=True)
    nama_status = Column(String)

    def __repr__(self):
        return "<StatusModel(id_status='%s', nama_status='%s')>" % (self.id_status, self.nama_status)


class ProductModel(Base):
    __tablename__ = 'products'

    id_produk = Column(Integer, autoincrement=True, primary_key=True)
    nama_produk = Column(String)
    harga = Column(Integer)

    # Menambahkan kolom kategori_id yang merupakan kunci asing ke tabel categories
    kategori_id = Column(Integer, ForeignKey('categories.id_kategori'))
    status_id = Column(Integer, ForeignKey('status.id_status'))

    # Mendefinisikan relasi dengan CategoryModel dan StatusModel
    kategori = relationship('CategoryModel', foreign_keys=[kategori_id])
    status = relationship('StatusModel', foreign_keys=[status_id])

    def __repr__(self):
        return "<ProdukModel(id_produk='%s', nama_produk='%s', harga='%s', kategori_id='%s', status_id='%s')>" % (self.id_produk, self.nama_produk, self.harga, self.kategori_id, self.status_id)
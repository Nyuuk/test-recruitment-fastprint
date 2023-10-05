from flask import Flask, render_template, jsonify, request
from models import ProductModel, CategoryModel, StatusModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fromAPI import start as stGetApi


app = Flask(__name__)

url_database = "mysql+mysqlconnector://root:1234@localhost/applicant_job_test"
engine = create_engine(url_database)


Session = sessionmaker(bind=engine)
session = Session()

@app.route('/api/refresh_data', methods=["GET"])
def refresh_data():
    stGetApi()
    return jsonify({"code": 200}), 200

@app.route('/api/products/getall', methods=["GET"])
def getAll():
    id_bisadijual = session.query(StatusModel).filter_by(nama_status="bisa dijual").first().id_status
    data = session.query(ProductModel).filter_by(status_id=id_bisadijual).all()
    
    data = [{
        "id_produk" : data.id_produk,
        "nama_produk" : data.nama_produk,
        "harga" : data.harga,
        "kategori_id" : session.query(CategoryModel).filter_by(id_kategori=data.kategori_id).first().nama_kategori,
        "status_id" : "bisa dijual"
    } for data in data]
    return jsonify({
        "data" : data,
        "code" : 200
    }), 200

@app.route('/api/products/<int:id>', methods=["PUT", "DELETE"])
def productsEdDel(id):
    dataRequest = []
    if request.headers.get('Content-Type') == "application/json":
        dataRequest = request.json
    else:
        dataRequest = request.form

    if request.method == "PUT":
        # Validasi Request
        if not dataRequest or not dataRequest.get('nama_produk'):
            return {
                "code" : 400,
                "message" : "Bad Request"
            }, 400
        
        # harga harus di isi  dan harus berupa angka
        if not dataRequest.get('harga'):
            return {
                "code" : 400,
                "message" : "Bad Request"
            }, 400
        if not dataRequest.get('harga').isdigit():
            return {
                "code" : 400,
                "message" : "Bad Request"
            }, 400


        dataDB = session.query(ProductModel).filter_by(id_produk=id).first()
        data = {
            "nama_produk" : dataRequest.get('nama_produk') or dataDB.nama_produk,
            "harga" : dataRequest.get('harga') or dataDB.harga,
            "kategori_id": dataRequest.get('kategori_id') or dataDB.kategori_id,
            "status_id": dataRequest.get('status_id') or dataDB.status_id
        }
        session.query(ProductModel).filter_by(id_produk=id).update(dataRequest)
        session.commit()
        return {
            "code" : 200
        }, 200
    elif request.method == "DELETE":
        session.query(ProductModel).filter_by(id_produk=id).delete()
        session.commit()
        return {
            "code" : 200
        }, 200

@app.route('/api/products/new', methods=["POST"])
def newProduct():
    dataRequest = []
    if request.headers.get('Content-Type') == "application/json":
        dataRequest = request.json
    else:
        dataRequest = request.form
    
    # Validasi Request
    if not dataRequest or not dataRequest.get('nama_produk'):
        return {
            "code" : 400,
            "message" : "Bad Request"
        }, 400
    
    # harga harus di isi  dan harus berupa angka
    if not dataRequest.get('harga'):
        return {
            "code" : 400,
            "message" : "Bad Request"
        }, 400
    if not dataRequest.get('harga').isdigit():
        return {
            "code" : 400,
            "message" : "Bad Request"
        }, 400
    
    # Validasi apakah nama_produk sudah ada
    dataDB = session.query(ProductModel).filter_by(nama_produk=dataRequest.get('nama_produk')).first()
    if dataDB:
        return {
            "code" : 400,
            "message" : "Bad Request"
        }, 400

    # new Product
    new_product = ProductModel(nama_produk=dataRequest.get('nama_produk'), harga=dataRequest.get('harga'), kategori_id=(dataRequest.get('kategori_id') or None), status_id=(dataRequest.get('status_id') or None))

    session.add(new_product)
    session.commit()
    return {
        "code" : 200
    }, 200

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
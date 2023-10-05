from flask import Flask, render_template, jsonify
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

@app.route('/api/getall', methods=["GET"])
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


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
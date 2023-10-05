import requests
import hashlib
import datetime
import json
from models import CategoryModel, StatusModel, ProductModel, url_database

from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

# Membuat object connection DB
engine = create_engine(url_database)
Session = sessionmaker(bind=engine)
session = Session()


def get_data_from_api():
    today = datetime.date.today()
    day = today.day
    month = today.month
    year = today.strftime("%y")

    string_password = "bisacoding-" + (str(day) if len(str(day)) > 1 else "0" + str(day)) + "-" + str(month) + "-" + str(year)

    # object md5 
    md5_hash = hashlib.md5()
    md5_hash.update(string_password.encode())
    md5_result = md5_hash.hexdigest()

    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    data = {
        "username": "asal",
        "password": md5_result
    }
    response = requests.post(url, data=data)

    Username = response.headers['X-Credentials-Username'].split(' ')[0]
    data['username'] = Username
    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return False


# check kategori apakah sudah ada di db, jika belum ada maka menambahkan kategori baru
def to_categori(datas):
    datasDB = session.query(CategoryModel.nama_kategori.label('nama_kategori')).all()
    dataDB = [data.nama_kategori for data in datasDB] 

    n = []
    for nama in datas:
        if nama in dataDB:
            continue
        else:
            if nama not in n:
                n.append(nama)
                session.add(CategoryModel(nama_kategori=nama))

    session.commit()

def to_status(datas):
    datasDB = session.query(StatusModel.nama_status).all()
    dataDB = [data[0] for data in datasDB]

    n = []
    for status in datas:
        if status in dataDB:
            continue
        else:
            if status not in n:
                n.append(status)
                session.add(StatusModel(nama_status=status))

    session.commit()

def to_product(datas):
    for data in datas:
        kategori_id = session.query(CategoryModel.id_kategori).filter(CategoryModel.nama_kategori == data['kategori']).first()[0]
        status_id = session.query(StatusModel.id_status).filter(StatusModel.nama_status == data['status']).first()[0]

        if not kategori_id:
            kategori_id = None
        if not status_id:
            status_id = None
        
        dataDB = session.query(ProductModel.id_produk).filter(ProductModel.nama_produk == data['nama_produk']).first()
        if dataDB:
            nama_produk = data.get('nama_produk') or dataDB.nama_produk
            harga = data.get('harga') or dataDB.nama_produk
            stmt = update(ProductModel).where(ProductModel.id_produk == dataDB.id_produk).values(nama_produk=nama_produk, harga=harga, kategori_id=kategori_id, status_id=status_id)
            session.execute(stmt)
            # print('data sudah ada', nama_produk, harga, kategori_id, status_id)
        else:
            session.add(ProductModel(nama_produk=data['nama_produk'], harga=data['harga'], kategori_id=kategori_id, status_id=status_id))
    
    session.commit()

# print(json.dumps(get_data_from_api(), indent=4))

def start():
    datas = get_data_from_api()['data']
    dataCategories = [data['kategori'] for data in datas]
    dataStatus = [data['status'] for data in datas]
    to_categori(dataCategories)
    to_status(dataStatus)
    to_product(datas)

#start()

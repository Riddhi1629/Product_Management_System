from flask import Flask
from flask_restful import Api

from resources.product import Product
from resources.geoprice import GeoPrice


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:khuri@1629@localhost/Product_Management_System'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='Riddhi'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Product, '/add/product', '/get/product/')
api.add_resource(GeoPrice, '/add/product/info', '/get/product/info')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
app.run(port=5935,debug=True)
from models.product import ProductModel
from flask_restful import Resource,reqparse
from flask import request
import redis

r=redis.Redis()

class GeoPrice(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('product_id',
        type=int,
        required=True,
        help="You must Enter product id!!"
    )

    parser.add_argument('price',
        type=int,
        required=True,
        help="You must Enter the price of the product!!"
    )

    parser.add_argument('stock',
        type=int,
        required=True,
        help="You must Enter the current stock of the product!!"
    )

    def post(self):
        recv_data=GeoPrice.parser.parse_args()
        if ProductModel.find_by_id(recv_data['product_id']):
            
            product_id=recv_data['product_id']
            data ={
                "price": recv_data['price'],
                "stock": recv_data['stock']
            }
            data=str(data)
            try:
                result=r.set("product_id/%d" %product_id, data)
            except:
                return {"message":"An Error occured while inserting the information!!"},500
            return {"message":"Successfully Entered the product details"},201

    def get(self):
        recv_data = request.get_json()
        
        if recv_data is not None:
            product=ProductModel.find_by_id(recv_data['product_id'])
            if ProductModel.find_by_id(recv_data['product_id']):
                product_id= recv_data['product_id']
                print(r.get("product_id/%d" %product_id))
                result= eval(r.get("product_id/%d" %product_id))
                return product.get_info()
            return {"message":"Product does not exist!!"},404

        else:
            return {'products':[product.get_info() for product in ProductModel.query.all()]}


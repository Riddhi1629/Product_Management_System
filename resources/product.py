from models.product import ProductModel
from flask_restful import Resource,reqparse
from flask import request


class Product(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('name',
        type=str,
        required=True,
        help="You must Enter the name of the product!!"
    )

    parser.add_argument('description',
        type=str,
        required=True,
        help="You must Enter the description of the product!!"
    )

    def post(self):
        
        recv_data=Product.parser.parse_args()

        if ProductModel.find_by_name(recv_data['name']):
            return {"message":"A product with the name {} already exists..".format(recv_data['name'])},400


        product=ProductModel(recv_data['name'], recv_data['description'])

        try:
            product.save_to_db()
        except:
            return {"message":"An Error occured while inserting the data!!"},500

        return product.json(),201

    def get(self):
        recv_data = request.get_json()
        if recv_data is not None:
            product=ProductModel.find_by_name(recv_data['name'])
            if ProductModel.find_by_name(recv_data['name']):
                return product.json()
            return {"message":"Product does not exist!!"},404

        else:
            return {'products':[product.json() for product in ProductModel.query.all()]}

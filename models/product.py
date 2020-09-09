from db import db
import redis

r=redis.Redis()

class ProductModel(db.Model):
    __tablename__='products'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))
    description = db.Column(db.String(255))


    def __init__(self, name, description):
        self.name=name
        self.description=description


    def json(self):
        return {'product_id': self.id, 'name': self.name, 'description': self.description}

    def get_info(self):
        result= eval(r.get("product_id/%d" %self.id))
        data = {
            'product_id': self.id,
            'name': self.name,
            'price': result['price'],
            'stock': result['stock']
        }
        return data


    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls,product_id):
        return cls.query.filter_by(id=product_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


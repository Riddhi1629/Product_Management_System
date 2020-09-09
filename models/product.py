from db import db
import redis

class ProductModel(db.Model):
    __tablename__='products'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))
    description = db.Column(db.String(255))


    def __init__(self, name, description):
        self.name=name
        self.description=description


    def json(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}

    def get_info(self):
        r=redis.Redis()
        # result=r.get("product_id/%d" %self.id)
        result= eval(r.get("product_id/%d" %self.id))
        data = {
            'id': self.id,
            'name': self.name,
            'price': result['price'],
            'stock': result['stock']
        }
        return data


    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()

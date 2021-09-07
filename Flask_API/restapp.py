from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource, abort, fields, marshal_with

app = Flask(__name__)

app.config["SECRET_KEY"] = "KEYTOSECRETS"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "price": fields.Float
}


# Modal class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


# Schema Class
class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "price")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class HelloWorld(Resource):
    # def get(self, id=None):
    #     if id is None:
    #         all_records = Product.query.all()
    #         rec = products_schema.dump(all_records)
    #         return jsonify(rec)
    #     else:
    #         record = Product.query.filter_by(id=id).first()
    #         if record:
    #             return product_schema.jsonify(record)
    #         else:
    #             abort(404, message="Record not found")
    @marshal_with(resource_fields)
    def get(self, id):
        record = Product.query.filter_by(id=id).first()
        if record:
            # return product_schema.jsonify(record)
            return record
        else:
            abort(404, message="Record not found")

    @marshal_with(resource_fields)
    def post(self, id):
        record = Product.query.filter_by(id=id).first()
        if record:
            abort(409, message="Id Already exists")
        id = request.json['id']
        name = request.json['name']
        price = request.json['price']
        new_record = Product(id, name, price)
        db.session.add(new_record)
        db.session.commit()
        # return product_schema.jsonify(new_record)
        return new_record

    @marshal_with(resource_fields)
    def put(self, id):
        record = Product.query.filter_by(id=id).first()
        if not record:
            abort(404, message="Id does not exists")
        record.id = request.json['id']
        record.name = request.json['name']
        record.price = request.json['price']

        db.session.commit()
        # return product_schema.jsonify(record)
        return record

    @marshal_with(resource_fields)
    def delete(self, id):
        record = Product.query.filter_by(id=id).first()
        if not record:
            abort(404, message="Id does not exists")

        db.session.delete(record)
        db.session.commit()
        # return product_schema.jsonify(record)
        return record


api.add_resource(HelloWorld, "/<id>")


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config["SECRECT_KEY"] = "VERYSECRETKEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


# Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))

    def __init__(self, title, description):
        self.title = title
        self.description = description


# Schema For Model
class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description")


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


@app.route("/get", methods=["GET"])
def get_post():
    all_records = Post.query.all()
    res = posts_schema.dump(all_records)
    return jsonify(res)


@app.route("/get/<id>", methods=["GET"])
def get_post_by_id(id):
    res = Post.query.get(id)
    return post_schema.jsonify(res)


@app.route("/post", methods=["POST"])
def insert_post():
    t = request.json["title"]
    d = request.json["description"]
    res = Post(title=t, description=d)
    db.session.add(res)
    db.session.commit()
    return post_schema.jsonify(res)


@app.route("/update/<int:id>", methods=["PUT"])
def edit_post(id):
    record = Post.query.get(id)
    record.title = request.json["title"]
    record.description = request.json["description"]

    db.session.commit()
    return post_schema.jsonify(record)


@app.route("/delete/<id>", methods=["DELETE"])
def del_post(id):
    record = Post.query.get(id)
    db.session.delete(record)
    db.session.commit()
    return post_schema.jsonify(record)


if __name__ == "__main__":
    app.run(debug=True)

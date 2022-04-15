from dataclasses import dataclass
import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from flask_restx import Api, Namespace, Resource

# from model import Port
from schema import PortSchema


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}/app-dev.db".format(basedir)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# import initdb
# initdb.init_db()
db.create_all()
db.session.commit()

@dataclass
class Port(db.Model):
    __tablename__ = "port"

    portId = db.Column(db.String(50), primary_key=True)
    # userId = db.Column(db.Integer, db.ForeignKey('user.userId'),
    #     nullable=False)
    # category = db.relationship('Category',
    #     backref=db.backref('posts', lazy=True))
    name = db.Column(db.String(255), unique=False, nullable=True)
    country = db.Column(db.String(255), unique=False, nullable=True)
    data =  db.Column(db.String(255), unique=False, nullable=True)

api = Api(app, version='1.0', title='Fieldwire API', description='Fieldwire API')
port_api = Namespace("Port", description="Port")
api.add_namespace(port_api, path=f"/port")




@port_api.route("")
class PortResource(Resource):
    def get(self):
        data = Port.query.get('AEAJM')
        # data = Port.query.all()
        # print(data)
        # res = PortSchema.dump(data)
        # print(res)
        # return {'Ports':jsonify(data), 'message':'Success' }, 200
        return {'Ports':{'name':data.name}, 'message':'Success'}, 200

if __name__ == "__main__":
    # db.create_all()
    # db.session.commit()
    app.run(debug=True)
from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message": "Store not found "}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "A Store with given name already exists"}

        store = StoreModel(name)
        store.save_to_db()
        return store.json(), 201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message": "Store deleted"}, 204
        return {"message": "Store not found "}, 404

class StoreList(Resource):
    def get(self):
        return {"stores":[store.json() for store in StoreModel.query.all()]}


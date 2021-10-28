from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.item import ItemModel

BLANK_ERROR = "'{}' cannot be left blank!"
ALREADY_EXISTS = "An item with name '{}' already exists"
ITEM_NOT_FOUND = "Item not found"
ERROR_INSERTING = "An error occured inserting the item"
ITEM_DELETED = "Item deleted"


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help=BLANK_ERROR.format("price")
    )

    parser.add_argument(
        "store_id", type=float, required=True,
        help=BLANK_ERROR.format("store_id")
    )

    def get(self, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": ITEM_NOT_FOUND}, 404

    @jwt_required(fresh=True)
    def post(self, name: str):
        if ItemModel.find_by_name(name):
            return {"message": ALREADY_EXISTS.format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except Exception:
            return {"message": ERROR_INSERTING}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": ITEM_DELETED}, 204
        return {"message": "Item with name not found"}, 404

    def put(self, name: str):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        items = [item.json() for item in ItemModel.find_all()]
        return {"items": items}

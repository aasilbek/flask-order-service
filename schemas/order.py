from ma import ma
from models.order import OrderModel
from models.item import ItemModel
from schemas.item import ItemSchema


class OrderSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)
    class Meta:
        model = OrderModel
        load_only = ("token",)
        dump_only = ("id", "status","items")
        load_instance = True

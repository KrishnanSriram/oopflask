from flask import Blueprint, jsonify, request
from handler import ItemHandler

class ItemRoutes:
    def __init__(self):
        self.blueprint = Blueprint('item_routes', __name__)
        self.handler = ItemHandler()
        self.add_routes()

    def add_routes(self):
        # self.blueprint.add_url_rule('/', 'home', self.home)
        self.blueprint.add_url_rule('/items', 'get_items', self.get_items, methods=['GET'])
        self.blueprint.add_url_rule('/items/<int:item_id>', 'get_item', self.get_item, methods=['GET'])
        self.blueprint.add_url_rule('/items', 'add_item', self.add_item, methods=['POST'])
        self.blueprint.add_url_rule('/items/<int:item_id>', 'update_item', self.update_item, methods=['PUT'])
        self.blueprint.add_url_rule('/items/<int:item_id>', 'delete_item', self.delete_item, methods=['DELETE'])
        # self.blueprint.add_url_rule('/health', 'health_check', self.health_check, methods=['GET'])

    # def home(self):
    #     return "Welcome to the Flask service!"

    def get_items(self):
        items = self.handler.get_items()
        return jsonify(items)

    def get_item(self, item_id):
        item = self.handler.get_item(item_id)
        if item:
            return jsonify(item)
        else:
            return "Item not found", 404

    def add_item(self):
        new_item = request.json.get('item')
        added_item = self.handler.add_item(new_item)
        return jsonify({"item": added_item}), 201

    def update_item(self, item_id):
        updated_item = request.json.get('item')
        result = self.handler.update_item(item_id, updated_item)
        if result:
            return jsonify({"item_id": item_id, "updated_item": result})
        else:
            return "Item not found", 404

    def delete_item(self, item_id):
        result = self.handler.delete_item(item_id)
        if result:
            return jsonify({"message": f"Item {item_id} deleted"}), 200
        else:
            return "Item not found", 404

    # def health_check(self):
    #     return jsonify({"status": "healthy"}), 200

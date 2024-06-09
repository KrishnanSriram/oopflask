class ItemHandler:
    def __init__(self):
        self.items = ["item1", "item2", "item3"]

    def get_items(self):
        return self.items

    def get_item(self, item_id):
        if 0 <= item_id < len(self.items):
            return self.items[item_id]
        else:
            return None

    def add_item(self, new_item):
        self.items.append(new_item)
        return new_item

    def update_item(self, item_id, updated_item):
        if 0 <= item_id < len(self.items):
            self.items[item_id] = updated_item
            return updated_item
        else:
            return None

    def delete_item(self, item_id):
        if 0 <= item_id < len(self.items):
            return self.items.pop(item_id)
        else:
            return None
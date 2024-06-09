from flask import Flask
from routes.item_routes import ItemRoutes
from routes.default_routes import HomeAndHealthRoutes

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.register_blueprints()

    def register_blueprints(self):
        item_routes = ItemRoutes()
        default_routes = HomeAndHealthRoutes()
        self.app.register_blueprint(item_routes.blueprint)
        self.app.register_blueprint(default_routes.blueprint)

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
        app = FlaskApp()
        app.run()
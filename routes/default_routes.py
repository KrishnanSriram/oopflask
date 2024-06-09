from flask import Blueprint, jsonify, request

class HomeAndHealthRoutes:
    def __init__(self) -> None:
        self.blueprint = Blueprint('homehealth_routes', __name__)
        self.add_routes()

    def add_routes(self):
        self.blueprint.add_url_rule('/', 'home', self.home)
        self.blueprint.add_url_rule('/health', 'health_check', self.health_check, methods=['GET'])

    def home(self):
        return jsonify({"message": "Welcome to the Flask service. Check out /items and /health routes for more"}), 200
    
    def health_check(self):
        return jsonify({"status": "healthy"}), 200
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from src.models.user import db

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///document_verification.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'

CORS(app,origins="*", methods=["GET", "POST", "PUT", "DELETE"])
db.init_app(app)  
jwt = JWTManager(app)

@app.get('/')
def hello():
    return jsonify({"message": "Hello, welcome to the website"}), HTTPStatus.OK

from src.controllers.auth_controller import auth
from src.controllers.document_controller import document
from src.models.user import User, db

app.register_blueprint(auth)
app.register_blueprint(document)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables in the database
    app.run(debug=True)

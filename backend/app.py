from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from auth import auth_bp
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://postgres:postgres@db:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return "👋 JWT Auth API is running!", 200
if __name__ == '__main__':
    app.run(host='0.0.0.0')


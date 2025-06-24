import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, get_jwt
from jwt.exceptions import ExpiredSignatureError
from config import Config
from controllers import guest_bp, episode_bp, appearance_bp, auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Late Show API'})

if __name__ == '__main__':
    app.run(debug=True)

    
 
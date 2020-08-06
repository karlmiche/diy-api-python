from models import app, User
from flask import jsonify

# home route!!
@app.route('/')
def home():
    return jsonify(message='welcome home!! 🧁')
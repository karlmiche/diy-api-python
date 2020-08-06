from models import app, Artist
from flask import jsonify

# home route!!
@app.route('/')
def home():
    return jsonify(message='welcome home!! 🧁')
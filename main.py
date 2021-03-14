from flask import jsonify, render_template
from app import app, db
from flask_cors import CORS

# включаем CORS для WebComponents
CORS(app)

from notes.blueprint import create_notes, update_notes, get_notes, delete_notes


# тут будем регистрировать Blueprints (приложения)
app.register_blueprint(create_notes, url_prefix='/notes')
app.register_blueprint(get_notes, url_prefix='/notes')
app.register_blueprint(update_notes, url_prefix='/notes')
app.register_blueprint(delete_notes, url_prefix='/notes')


@app.errorhandler(404)
def error404(error):
    return jsonify({"error": "404"}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0')

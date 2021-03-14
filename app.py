from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

SWAGGER_URL = '/swagger'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    '/static/api_swagger.yaml',
    config={
        'app_name': "api-swagger"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


app.config.from_object(Config)

db = MongoEngine(app)
db.connect(**Config.MONGODB_SETTINGS)
app.session_interface = MongoEngineSessionInterface(db)

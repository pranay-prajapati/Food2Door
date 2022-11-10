from database.db_config import DatabaseConfig
from database.db_creator import PostgresHandler
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

db_passcode = DatabaseConfig.password.replace("%", "%%")
handler = PostgresHandler(
    DatabaseConfig.host,
    DatabaseConfig.username,
    DatabaseConfig.password,
    DatabaseConfig.port,
    DatabaseConfig.database_name,
    DatabaseConfig.pool_size,
)


def create_model():
    print("Initializing.....")
    handler.initialize_db()
    app.config['MONGODB_SETTINGS'] = {
        'db': DatabaseConfig.mongodb_name,
        'host': 'localhost',
        'port': DatabaseConfig.mongodb_port
    }
    db = MongoEngine()
    db.init_app(app)

    from models.user_model import User
    from models.food_management import RestaurantReview, DeliveryAgentReview
    from models import payment_management, food_management
    handler.Base.metadata.create_all(bind=handler.engine)

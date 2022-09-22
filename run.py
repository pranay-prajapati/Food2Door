from flask import Flask
import os
from database import db_models

app = Flask(__name__)
db_models.create_model()

if __name__ == "__main__":
    os.system("alembic upgrade head")  # upgrade database to latest version
    print("started..............")
    app.run(host="0.0.0.0", port=8000, debug=True)

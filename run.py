from flask import Flask
import os
from database import db_models

app = Flask(__name__)
db_models.create_model()
if __name__ == "__main__":
    # os.system("alembic upgrade head")  # upgrade database to latest version
    # app = create_app()
    print("started..............")
    app.run(debug=True)
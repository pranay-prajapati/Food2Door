from flask import Flask
import os
from database import db_models
import pathlib
from service import create_app

absolute_path = str(pathlib.Path(__file__).parent.absolute()) + "/alembic.ini"

# app = Flask(__name__)
db_models.create_model()
app = create_app()

if __name__ == "__main__":

    os.system(f"alembic -c {absolute_path} upgrade head")  # upgrade database to latest version
    print("started..............")
    app.run(host="0.0.0.0", port=8000, debug=True)

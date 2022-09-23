from flask import Flask
import os
from database import db_models
import pathlib
from constants.constant import ALEMBIC_PATH

absolute_path = str(pathlib.Path(__file__).parent.absolute()) + "/database/alembic.ini"

app = Flask(__name__)
db_models.create_model()

if __name__ == "__main__":

    os.system(f"alembic -c {ALEMBIC_PATH} upgrade head")  # upgrade database to latest version
    print("started..............")
    app.run(host="0.0.0.0", port=8000, debug=True)

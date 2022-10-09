from flask import json
import werkzeug.routing as r
from app import app


def see_json():
    data = app.api.as_postman(urlvars=False, swagger=True)
    print(json.dumps(data))

with app.app_context():
    see_json()
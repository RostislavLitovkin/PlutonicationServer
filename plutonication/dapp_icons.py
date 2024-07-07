from flask import send_file
from .extensions import app


@app.route("/dapp/hydration-icon")
def hydration_icon():
    return send_file("static/dapp_icons/hydration.png", mimetype='image/png')


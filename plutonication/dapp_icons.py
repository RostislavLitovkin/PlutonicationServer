from flask import send_file
from .extensions import app


@app.route("/dapp/hydration-icon")
def hydration_icon():
    return send_file("static/dapp_icons/hydration.png", mimetype="image/png")


@app.route("/dapp/mimir-icon")
def mimir_icon():
    return send_file("static/dapp_icons/mimir.png", mimetype="image/png")


@app.route("/dapp/astar")
def astar_icon():
    return send_file("static/dapp_icons/astar.png", mimetype="image/png")


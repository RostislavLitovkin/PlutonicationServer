from flask import send_file
from .dapp_icons import app


@app.route("/wallets/plutowallet")
@app.route("/wallets/plutowalletwhite")
def plutowallet_white_icon():
    return send_file("static/wallet_icons/plutowallet-icon-white.png", mimetype='image/png')


@app.route("/wallets/plutowalletblack")
def plutowallet_black_icon():
    return send_file("static/wallet_icons/plutowallet-icon-black.png", mimetype='image/png')


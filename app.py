import json
import os

import requests
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap

from config import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key-just-for-testing"
Bootstrap(app)
auth_token = None


@app.route("/")
def home():
    if auth_token is None:
        return render_template(
            "hello.html", showme={"Tips:": "click the login with mixin button."}
        )
    return render_template("hello.html", showme={"Tips:": "welcome back!"})


@app.route("/login")
def login():
    """login with mixin"""
    return redirect(MIXIN_AUTH_URL, 302)


@app.route("/callback", methods=["POST", "GET"])
def oauth2_callback():
    post_data = {
        "client_id": MIXIN_CLIENT_ID,
        "code": request.args.get("code"),
        "client_secret": MIXIN_CLIENT_SECRET,
    }
    resp = requests.post(
        MIXIN_AUTH_TOKEN_URL, json=post_data, headers={"Accept": "application/json"}
    )
    global auth_token
    auth_token = resp.json().get("data", {}).get("access_token")
    return redirect(url_for("user_profile"))


@app.route("/me", methods=["POST", "GET"])
def user_profile():
    if auth_token is None:
        return redirect(url_for("login"))

    api = "".join([MIXIN_BASEURL, "me"])
    header = {"Accept": "application/json", "Authorization": "Bearer " + auth_token}
    r_json = requests.get(api, headers=header).json()
    profile = {
        "user_id": r_json["data"]["user_id"],
        "full_name": r_json["data"]["full_name"],
        "avatar_url": r_json["data"]["avatar_url"],
    }
    return render_template("hello.html", showme=profile)


if __name__ == "__main__":
    app.config.update(DEBUG=True)
    app.run(debug=True)

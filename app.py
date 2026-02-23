import identity.flask
import requests
from flask import Flask, redirect, render_template, url_for
from flask_session import Session

import app_config

app = Flask(__name__)
app.config.from_object(app_config)
Session(app)

auth = identity.flask.Auth(
    app,
    authority=app.config["AUTHORITY"],
    client_id=app.config["CLIENT_ID"],
    client_credential=app.config["CLIENT_SECRET"],
    redirect_uri=app_config.REDIRECT_URI,
)


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/profile")
@auth.login_required(scopes=app_config.SCOPE)
def profile(*, context):
    # context contains user info + access_token (because we requested scopes)
    user = context["user"]

    # Call Graph API for full profile
    graph_response = requests.get(
        "https://graph.microsoft.com/v1.0/me",
        headers={"Authorization": f"Bearer {context['access_token']}"},
        timeout=10,
    ).json()

    return render_template("index.html", user=user, profile=graph_response)


@app.route("/login")
def login():
    return auth.login(scopes=app_config.SCOPE, next_link=url_for("profile"))


@app.route("/logout")
def logout():
    return redirect(auth.logout(url_for("index", _external=True)))


if __name__ == "__main__":
    app.run(debug=True, port=5002)

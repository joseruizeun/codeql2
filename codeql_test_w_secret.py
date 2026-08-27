import os
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)

# NOTE: Not a real credential.
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"


@app.route("/run")
def run_command():
    user_input = request.args.get("cmd", "")

    # NOTE: intentionally vulnerable for CodeQL SAST scanner validation (test fixture only)
    subprocess.run("echo " + user_input, shell=True, check=False)

    return "done"


@app.route("/user")
def get_user():
    db_path = "users.db"
    username = request.args.get("username", "")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # NOTE: intentionally vulnerable for CodeQL SAST scanner validation (test fixture only)
    query = "SELECT * FROM users WHERE name = '" + username + "'"

    cursor.execute(query)

    return str(cursor.fetchall())


if __name__ == "__main__":
    app.run()

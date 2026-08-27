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

    # Execute without invoking a shell to prevent command injection
    subprocess.run(["echo", user_input], check=False)

    return "done"


@app.route("/user")
def get_user():
    db_path = "users.db"
    username = request.args.get("username", "")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE name = ?"

    cursor.execute(query, (username,))

    return str(cursor.fetchall())


if __name__ == "__main__":
    app.run()

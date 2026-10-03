from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route("/")
def homePage():
    return render_template("homepage.html")

@app.route("/difficulty", methods=["GET", "POST"])
def difficultySelection():
    if request.method == "POST":
        difficulty = request.form["difficulty"] # Get the selected difficulty from the form
        return redirect(url_for("game"))
    return render_template("difficulty.html") 

@app.route("/game", methods=["GET", "POST"])
def game():
    return render_template("game.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # OS provides PORT
    app.run(host="0.0.0.0", port=port, debug=False)
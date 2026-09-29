from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("homepage.html")

@app.route("/difficulty")
def difficultySelection():
    return render_template("difficulty.html")

if __name__ == "__main__":
    app.run()
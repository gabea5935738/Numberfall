from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("homepage.html")

@app.route("/difficulty")
def difficultySelection():
    return render_template("difficulty.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port, debug=False)
from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    session,
    flash,
)
from chatbot2 import answer_question

app = Flask(__name__)
app.secret_key = "secret_key"

# Sample user data for demonstration purposes
users = {
    "user1": "password1",
}


@app.route("/")
def home():
    if "username" in session:
        return render_template("chat.html")
    return redirect(url_for("login"))


@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json["question"]
    answer = answer_question(user_question)
    return jsonify({"answer": answer})


@app.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["username"] = username
            flash("Login successful!")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials. Please try again.")
    return render_template("login.html")


@app.route("/auth/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

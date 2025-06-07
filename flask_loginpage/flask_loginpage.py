from flask import Flask, session, request, Response, url_for, redirect

app = Flask(__name__)
app.secret_key="supersecret"

# HomePage login Page
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "riooo@123" and password == "123":
            session["user"] = username #Stores in session
            return redirect(url_for("welcome"))
        return Response("Invalid credentials!! try again",mimetype="plain/text")
    
    return '''
            <h2>Login Page</h2>
            <form method="POST">
            username: <input type="text" name="username"><br>
            password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
            </form>

'''

# Welcome page(after login)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href={url_for("logout")}>Logout</a>
    '''
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
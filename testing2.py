from flask import Flask
app=Flask(__name__)
@app.route("/")
def testing2():
    return "Welcome to my page!"

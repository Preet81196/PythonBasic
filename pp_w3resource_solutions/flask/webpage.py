from flask import Flask
app = Flask(__name__)
@app.route("/")

def welcome():
    return "my first webpage"

if __name__ == "__main__":
    app.run()
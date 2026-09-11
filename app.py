from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Helow Uordi"

@app.route("/secret")
def reveal_secret():
  return "Secret Reveled"

if __name__ == "__main__":
  app.run(debug=True)
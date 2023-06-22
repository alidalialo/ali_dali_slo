from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return("Hello from Flask")

@app.route("/name")
def name():
    return("Hello friend")
    
if __name__=="__main__":
    app.run()
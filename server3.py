from flask import *

app = Flask(__name__)

@app.route("/")
def message():
    return(render_template("message.html"))

if __name__=="__main__":
    app.run(port=4444)
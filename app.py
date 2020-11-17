from flask import Flask

app: Flask = Flask(__name__)

@app.route("/")
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"

if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app


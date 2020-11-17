import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    color = os.environ.get('COLOR', "green")
    message = "Welcome !!! This is "+color+" environment"
    return message

@app.route('/hello')
def hello():
    return 'Hello World!!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


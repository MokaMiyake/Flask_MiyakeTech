from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello,こんにちは"

if __name__ == '__main__':
    debug = True
    app.run()


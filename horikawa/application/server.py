from flask_blog import app

print("server.py内の__name__は、「" + __name__ + "」")
if __name__ == "__main__":
    app.run()

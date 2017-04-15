from flask_script import Manager
from micro import create_app

app = create_app()
manager = Manager(app)


@app.route("/")
def hello():
    return "Hello World! v2"


if __name__ == '__main__':
    manager.run()

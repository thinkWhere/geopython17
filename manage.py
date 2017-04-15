from flask_script import Manager
from micro import create_app

app = create_app()
manager = Manager(app)


@app.route("/")
def welcome():
    return "Geopython 2017 Microservice"


if __name__ == '__main__':
    manager.run()

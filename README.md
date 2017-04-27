# GeoPython 2017
## Intro
This repo contains the accompanying code from the **Build your own Geospatial Microservice using Python/Flask/PostGIS** workshop thinkWhere gave at GeoPython 2017

## Dependencies
Following must be available locally:

* Python 3.6 - [Python 3.6 install here](https://www.python.org/downloads/)

### Optional 
The sample app ships with a Dockerfile that allows you to run PostGIS within a Docker container.  Alternatively if you have access to an existing PostGIS db you can connect the application to a new database there.

* [Docker CE install here](https://www.docker.com/community-edition#/download)

## Building the Microservice

* Create a Python Virtual Environment, using Python 3.6:
    * ```python -m venv ./venv```
* Activate your virtual environment and install dependencies:
    * Linux/Mac:
        * ```. ./venv/bin/activate```
        * ```pip install -r requirements.txt```
    * Windows (use installer because of precompiled libs):
        * ```.\venv\scripts\activate```
        * ```pip install -r requirements.txt```
        
## Build and run the PostGIS Dockerfile 

* From the root of the project:
    * ```docker build -t geopython-db ./devops/docker```
* The image should be downloaded and build locally. Once complete you should see it listed, with
    * ```docker images```
* You can now run the image (this will run PostGIS in a docker container, with port 5432 mapped to localhost):
    * ```docker run -d -p 5432:5432 geopython-db```
* Confirm the image is running successfully:
    * ```docker ps```

### App Config (only required if not using Docker PostGIS)
If you are not using the supplied PostGIS docker container you will need to set the SQLALCHEMY_DATABASE_URI found in ./micro/config.py to point to your database, eg:
 
```SQLALCHEMY_DATABASE_URI=postgresql://user:pass@host/your-new-database```

## Creating the DB
With everything now setup We use [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) to create the database from the migrations directory.  Create the database as follows:

```
python manage.py db upgrade
```

## Running Locally
Finally we can run the application, as follows:

```
python manage.py runserver -d
```

### Versions

You can see how we got to the version from Flask hello world to v1.0 of our microservice by checking out the tagged releases as follows:

``` git checkout -b version1 v0.1```

It may help to run git clean to tidy up any empty dirs for clarity as you work thru the versions, eg:

``` git clean -fd ```

### Useful Links

* [Flask](http://flask.pocoo.org/)
* [Flask-Script](https://flask-script.readthedocs.io/en/latest/)

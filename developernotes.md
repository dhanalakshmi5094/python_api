#Candidate notes here

Requirements:


Python (3.5, 3.6, 3.7, 3.8)
Django (3.0, 3.1)
Django REST Framework (3.11)

Install MongoDB server

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

Install MongoDB Compass

https://www.mongodb.com/download-center/community?jmp=docs


Running the api app:


It is recommended to create a virtualenv for testing. Assuming it is already installed and activated:

$ cd python_api


Installation:


$ pip install -r requirements.txt


Apply migrations with the below comamnds.Migrations only applied on default model such as Auth user, group, permission and not for django custom models in mongoengine:

$ python manage.py makemigrations
$ python manage.py migrate

create super user with the below command:

$ python manage.py createsuperuser


open browser:

http://localhost:8000/mongoadmin[login with superuser credentials]

open MongoDB Compass UI and create database with name "pythonapidb".

change the databases in settings.py [python_api/python_api/settings.py].

MONGODB_DATABASES = {
    'default': {'name': 'pythonapidb'}
}

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'pythonapidb',
    }
}

create collections and add data by uploading  json files [api/fixtures].


Run the Server:

$ python manage.py runserver

open browser:

Endpoint `/users` should return a collection of users:

http://localhost:8000/users

Endpoint `/assets` should return a collection of assets:

http://localhost:8000/assets

Endpoint `/scans` should return a collection of scans:

http://localhost:8000/scans

Endpoint `/vulnerabilities` should return a collection of vulnerabilities:

http://localhost:8000/vulnerabilities



#cartremind
[![Build Status](https://travis-ci.org/tkrevh/cartremind-api.svg?branch=master)](https://travis-ci.org/tkrevh/cartremind-api)

SaaS product, to track website visitors requests to be notified of specific events on any website. Suitable for eCommerce, SaaS, and other user facing websites and apps.. Check out the project's [documentation](http://tkrevh.github.io/cartremind-api/).

# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)
- [redis](http://redis.io/)
- [travis cli](http://blog.travis-ci.com/2013-01-14-new-client/)
- [heroku toolbelt](https://toolbelt.heroku.com/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

```bash
createdb cartremind
```
Initialize the git repository

```
git init
git remote add origin git@github.com:tkrevh/cartremind-api.git
```

Migrate, create a superuser, and run the server:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# Create Servers
By default the included fabfile will setup three environments:

- dev -- The bleeding edge of development
- qa -- For quality assurance testing
- prod -- For the live application

Create these servers on Heroku with:

```bash
fab init
```

# Automated Deployment
Deployment is handled via Travis. When builds pass Travis will automatically deploy that branch to Heroku. Enable this with:
```bash
travis encrypt $(heroku auth:token) --add deploy.api_key
```

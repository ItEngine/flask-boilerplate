Flask-Boilerplate
=================

Boilerplate for Flask with MVC pattern.

Getting started
---------------

1. Clone this repo.
2. Execute pip install -r requirements.txt.
3. Rename file conf/config_local.py.txt to conf/config_local.py and modify content file.
4. Execute in folder static npm install.
5. Execute python manage.py runserver and go to browser localhost:5000.
6. Run migrations
7. For create super user execute python manage.py createsuperuser.
8. Execute admin localhost:5000/admin.

Migrations command
------------------

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

Content
-------

1. Basic MVC structure.
2. Model USER integrate.
3. It contains the forms login, register and forgot password. Using flask-login.
4. Admin generator using flask-admin.
5. API REST with flask-restful.
6. Migrations with flask-migrate.
7. Shell with python manage.py shell.
8. Orm with SQLAlchemy.
9. Bootstrap and Jquery.
10. PostgreSql and Sqlite configuration.
11. Email configuration with flask-email.

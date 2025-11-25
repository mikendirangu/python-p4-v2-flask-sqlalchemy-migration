# server/app.py

from flask import Flask
from flask_migrate import Migrate

from models import db

# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
# This code sets up a Flask application with SQLAlchemy for database management and Flask-Migrate for handling database migrations. The application is configured to use a SQLite database stored in a local file named `app.db`, and it runs on port 5555 with debug mode enabled.
# The `db` object is initialized with the Flask application, allowing it to manage database operations
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # Load environment variables from .env file
    load_dotenv()

    # Print out environment variables
    print("DATABASE_URL:", os.environ.get('DATABASE_URL'))
    print("SECRET_KEY:", os.environ.get('SECRET_KEY'))
    print("JWT_SECRET_KEY:", os.environ.get('JWT_SECRET_KEY'))
    
    # # Load configuration from environment variables
    # app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    migrate.init_app(app, db)

    from . import routes
    app.register_blueprint(routes.bp)

    return app

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import os
# from dotenv import load_dotenv

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     # app.config.from_object('config.Config')

#     load_dotenv()

#     # Print out environment variables
#     print("DATABASE_URL:", os.environ.get('DATABASE_URL'))
#     print("SECRET_KEY:", os.environ.get('SECRET_KEY'))
#     print("JWT_SECRET_KEY:", os.environ.get('JWT_SECRET_KEY'))
    
#     # Load configuration from environment variables
#     app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')


#     db.init_app(app)
#     migrate.init_app(app, db)

#     from .routes import bp as api_bp  # Importing blueprint instance
#     app.register_blueprint(api_bp, url_prefix='/api')  # Registering blueprint with prefix

#     return app

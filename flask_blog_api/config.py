import os

class Config:
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret'

    # SECRET_KEY = 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/flask_blog'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT_SECRET_KEY = 'super-secret'
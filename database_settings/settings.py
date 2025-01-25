from flask_sqlalchemy import SQLAlchemy

def get_db(app, path_to_db):
    """Функция подключения к БД"""
    app.config['SQLALCHEMY_DATABASE_URI'] = path_to_db
    db = SQLAlchemy(app)
    return db



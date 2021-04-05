import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DDx@dazkHJ6H8&^^pXwSaBQUxWzJH@'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacizooserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacizoo'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'joshyjoshy'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Password1!'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    # SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacizoo'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '5/8V6DT1y2VkrV87B6jH7Y2EYgL02PM6geuMKhzQ5mPzhBnTXe9XEsz0NQFu1UqH2Ifr4JeHBOC3rs6TfgT+vA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

import os
DEBUG = True


# session 加密從random
# SECRET_KEY = os.urandom(24)
SECRET_KEY = '開發時固定'

# 連接資料庫
DIALECT = 'postgresql'
DRIVER = 'psycopg2'
USERNAME = 'postgres'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '5432'
DATABASE = 'mcs'
DB_URI = "{}+{}://{}:{}@{}:{}/{}?client_encoding=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True

BINDS_DATABASE = 'mock_pos'
DB_BINDS_URI = "{}+{}://{}:{}@{}:{}/{}?client_encoding=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT
                                                                    , BINDS_DATABASE)
SQLALCHEMY_BINDS = {
    "pos": DB_BINDS_URI
}

MC_USER_ID = 'XXX'
FRONT_USER_ID = 'YYY'

# flask mail設置
MAIL_SERVER = 'smtp.office365.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True
MAIL_USERNAME = 'coreyteng@hotmail.com'
MAIL_PASSWORD= 'XXXXX'
MAIL_DEFAULT_SENDER = 'coreyteng@hotmail.com'

# flask-paginate的相关配置
PER_PAGE = 10

# celery相关的配置
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"

# flask_apscheduler設置
SCHEDULER_API_ENABLED = True

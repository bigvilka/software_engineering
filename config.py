class Config:
    SECRET_KEY = 'smscrtk'
    DEBUG = True
    MONGO_USER = 'admin'
    MONGO_PASSWORD = 'admin'
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27019
    MONGO_DB_ADMIN = 'admin'
    MONGO_DB_REQUESTS = 'admin'
    MONGODB_SETTINGS = {
        'host': MONGO_HOST,
        'port': MONGO_PORT,
        'db': MONGO_DB_ADMIN,
        'username': MONGO_USER,
        'password': MONGO_PASSWORD
    }
    LOGSTASH_HOST = '0.0.0.0'
    LOGSTASH_PORT = 5006

    COUNT_OF_FIRST_N_LETTERS = 5
import os
from datetime import datetime, timedelta
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Common configurations
    """
    SECRET_KEY = os.environ.get("SECRET_KEY", None)

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", None)
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_EXPIRATION_DELTA", None)) # in seconds
    JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", None)

    # PARA HABILITAR JWT CON USO DE COOKIES
    JWT_TOKEN_LOCATION = os.environ.get("JWT_TOKEN_LOCATION", None)   # Buscar el token en cookies o headers (headers)
    JWT_ACCESS_COOKIE_NAME = os.environ.get("JWT_ACCESS_COOKIE_NAME", None)  # Nombre de la cookie
    JWT_COOKIE_SECURE = os.environ.get("JWT_COOKIE_SECURE", False)          # True si usas HTTPS
    JWT_COOKIE_CSRF_PROTECT = os.environ.get("JWT_COOKIE_CSRF_PROTECT", True)     # Protección CSRF

    # PARA HABILITAR JWT CON USO DE HEADERS
    #JWT_TOKEN_LOCATION = ["headers"] # Buscar el token en el header Authorization
    #JWT_HEADER_NAME = "Authorization" # Nombre del header esperado
    #JWT_HEADER_TYPE = "Bearer" # Prefijo que debe tener el token en el header

    SQLALCHEMY_ENGINE_OPTIONS = { "poolclass": NullPool }
    CORS_EXPOSE_HEADERS = ["Content-Disposition"]


class DevConfig(Config):
    """
    Development configurations
    """
    #FLASK
    FLASK_DEBUG = True
    #SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = f'{os.environ.get("DB_DEV")}/SCHEMA_NAME'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_BINDS = {
        'db_name_bind': f'{os.environ.get("DB_DEV_BIND")}/SCHEMA_NAME',
    }

    SQLALCHEMY_ECHO = True
    SENTRY_ENV = "development"


class QaConfig(Config):
    """
    QA Ambient configurations
    """
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'{os.environ.get("DB_QA")}/SCHEMA_NAME'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'db_name_bind': f'{os.environ.get("DB_QA_BIND")}/SCHEMA_NAME',
    }
    SENTRY_ENV = "release"


class ProdConfig(Config):
    """
    Production configurations
    """

    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'{os.environ.get("DB_PRD")}/SCHEMA_NAME'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'db_name_bind': f'{os.environ.get("DB_PRD_BIND")}/SCHEMA_NAME',
    }
    SENTRY_ENV = "production"



app_config = {
    'dev': DevConfig,
    'qa': QaConfig,
    'pro': ProdConfig
}

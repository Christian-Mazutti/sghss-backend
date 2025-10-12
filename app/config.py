import os

class Config:
    # Configurações básicas. Em produção, use variáveis seguras.
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///sghss.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'dev_jwt_secret')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/app.log')

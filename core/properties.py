import telebot

bot = telebot.TeleBot('TOKEN')


# Настройки брокера для сельдерея
REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'
REDIS_PASSWORD = '5MjXwTrA6Hy6JZSOv7XYkV1M6'


# REDIS_BROKER = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0'
REDIS_BROKER = 'redis://redis:6379/0'
# REDIS_BACKEND = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0'
REDIS_BACKEND = 'redis://redis:6379/0'
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:6512@db:5432/postgres"
# Ключ доступа к API
FLAMP_API_KEY = 'Bearer 2b93f266f6a4df2bb7a196bb76dca60181ea3b37'

DOUBLE_GIS_API_KEY = '37c04fe6-a560-4549-b459-02309cf643ad&locale'

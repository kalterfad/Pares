import telebot

bot = telebot.TeleBot('5551940599:AAG6D5XJXMXleud8ZPe48LXVsVnTiPA8xOc')


# Настройки брокера для сельдерея
REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'
REDIS_PASSWORD = '5MjXwTrA6Hy6JZSOv7XYkV1M6'

# redis://:password@hostname:port/db_number

# REDIS_BROKER = 'redis://'+ REDIS_PASSWORD + '@' + REDIS_HOST + ':' + REDIS_PORT + '/0'
REDIS_BROKER = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0'
# REDIS_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
REDIS_BACKEND = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0'

# Ключ доступа к API
FLAMP_API_KEY = 'Bearer 2b93f266f6a4df2bb7a196bb76dca60181ea3b37'
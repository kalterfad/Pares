from app.face_control import Controller as control

from app.core.properties import bot


@bot.message_handler(commands=['start'])
@control('ban')
def send_welcome(message):
    # bot.send_sticker(message.chat.id, process.get_sticker('hello'))
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}, '
                     'Выбери команду для продолжения или напиши /help.'.
                     format(message.from_user, bot.get_me()), parse_mode='html')

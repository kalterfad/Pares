import re

from app.bot_process import create_new_user
from app.core.properties import bot
from app.crud import update_user_data
from app.face_control import Controller as control
from app.keyboard import Keyboard
from app.schemas import UserBase


@bot.message_handler(commands=['start'])
@control('ban')
def send_welcome(message):

    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}.\n\n'
                     'Заявка на верификацию направлена администратору.'.
                     format(message.from_user, bot.get_me()), parse_mode='html')

    create_new_user(UserBase(**{
        'id': message.chat.id,
        'username': message.from_user.first_name,
        'is_active': False,
        'is_superuser': False
    }))
    send_admin_message(message)


def send_admin_message(message):
    """Отправляет админу сообщение о вступлении нового пользователя"""

    text = f'Пользователь запросил подтверждение аккаунта\n\n' \
           f'Ник: <b>{message.from_user.first_name}</b>\n' \
           f'Чат id: <b>{message.chat.id}</b>'

    markup = Keyboard(
        message.chat.id,
        is_active_actions='Активировать',
        is_superuser_actions='Дать права администратора').user_right_keyboard()

    # Кидаем запрос на получение айди всех админов, после чего рассылаем сообщения
    # all_users = get_all_users()

    bot.send_message(446777294, text=text, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data[:3] == 'is_')
def issue_rights(call):
    """Функция для выдачи или отзыва прав пользователя"""

    chat_id = re.search('id.*?(\d+)', str(call.data)).group(1)
    # is_active | is_superuser
    action = call.data.partition('_id')[0]
    # Действие, на которое нажал админ, ниже через него достаются следующие данные:
    # Активировать | Деактивировать, Дать права админа |  Отозвать права админа
    selected_action = call.json["message"]["reply_markup"]["inline_keyboard"][0]
    # Словарь содержатся возможные действия над пользователем
    action_dict = {
        'Активировать': ['Деактивировать', 'Пользователь активирован', True],
        'Деактивировать': ['Активировать', 'Пользователь деактивирован', False],
        'Дать права администратора': ['Отозвать права администратора', 'Пользователю выданы права администратора',
                                      True],
        'Отозвать права администратора': ['Дать права администратора', 'Права администратора отозваны', False]
    }
    # В словаре содержится нажатое админом действие, которое необходимо выполнить над пользователем
    right_dict = {
        'is_active': {
            'message': f'Пользователь: {chat_id}\n\n<b>{action_dict[selected_action[0]["text"]][1]}</b>',
            'active': action_dict[selected_action[0]['text']][0],
            'superuser': selected_action[1]['text'],
            'action': selected_action[0]["text"]
        },
        'is_superuser': {
            'message': f'Пользователь: {chat_id}\n\n<b>{action_dict[selected_action[1]["text"]][1]}</b>',
            'active': selected_action[0]['text'],
            'superuser': action_dict[selected_action[1]['text']][0],
            'action': selected_action[1]["text"]
        }
    }

    update_user_data(chat_id, update_data={action: action_dict[right_dict[action]['action']][2]})
    bot.answer_callback_query(call.id, 'Успешно', show_alert=False)

    markup = Keyboard(chat_id, right_dict[action]['active'], right_dict[action]['superuser']).user_right_keyboard()
    bot.edit_message_text(right_dict[action]['message'], call.from_user.id, call.message.message_id, parse_mode='html',
                          reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)

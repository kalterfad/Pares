import telebot
token = '1798617244:AAEKjRPh8qNY9lw4b77Hd_p7TGVkvyCqSJs'

bot = telebot.TeleBot(token)


@bot.callback_query_handler(func=lambda call: call.data != 1)
def a(call):
    print(call.data)



if __name__ == '__main__':
    bot.polling(none_stop=True)
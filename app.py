import data
import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def babu(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('start')
    markup.add(itembtn1)

    bot.send_message(message.chat.id, 'Hello user this is "Capital city" game where you should find capital city of country. Good Luck  🤗 ', reply_markup=markup)


cities_data_correct_answer = []
@bot.message_handler()
def start_game(message):
    cities_data_correct_answer.clear()
    if message.text == 'start' or 'Keep playing':
        country_name = data.randdom_country()
        cities_data_array = data.cities_names(country_name)['array']
        cities_data_answer = data.cities_names(country_name)['answer']
        #ask to the Shoxruz aka can i do it more better
        cities_data_correct_answer.append(cities_data_answer)
        #creation new buttons
        markup = types.InlineKeyboardMarkup()
        answer1 = types.InlineKeyboardButton(cities_data_array[0], callback_data=cities_data_array[0])
        answer2 = types.InlineKeyboardButton(cities_data_array[1], callback_data=cities_data_array[1])
        answer3 = types.InlineKeyboardButton(cities_data_array[2], callback_data=cities_data_array[2])
        markup.add(answer1, answer2, answer3)
        bot.send_message(message.chat.id, 'What is capital city of ' + country_name , reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    markup = types.ReplyKeyboardMarkup()
    item_1 = types.KeyboardButton('Keep playing')
    markup.add(item_1)
    if call.message:
        if call.data == cities_data_correct_answer[0]:
            bot.send_message(call.message.chat.id, 'Correct' , reply_markup=markup)
            cities_data_correct_answer.clear()
        else:
            bot.send_message(call.message.chat.id, 'Incorrect ' + 'correct answer is ' + cities_data_correct_answer[0], reply_markup=markup)
            cities_data_correct_answer.clear()









bot.infinity_polling()
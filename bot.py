import telebot
from config import TOKEN, QUESTIONS, RESULTS
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_data[message.chat.id] = {"score": {}, "current_question": 0}
    bot.send_message(
        message.chat.id,
        "Привет! Узнай своё тотемное животное в Московском зоопарке 🐾\n\nНажми кнопку ниже, чтобы начать викторину!",
        reply_markup=start_keyboard()
    )

def start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Начать викторину"))
    return keyboard



bot.polling()
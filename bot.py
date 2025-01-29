import telebot
from config import TOKEN, QUESTIONS, RESULTS
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    start_button = InlineKeyboardButton("Начать викторину", callback_data="start_quiz")
    markup.add(start_button)

    user_data[message.chat.id] = {"score": {}, "current_question": 0}
    bot.send_message(
        message.chat.id,
        """Привет! 👋
Добро пожаловать в увлекательную викторину, где ты узнаешь, какое тотемное животное скрывается внутри тебя! 🐾
Московский зоопарк приглашает тебя на это забавное и познавательное путешествие по миру животных. В процессе викторины ты познакомишься с интересными фактами и уникальными особенностями обитателей нашего зоопарка. 🦁🐧🐯
А ещё — возможно, ты станешь опекуном одного из этих удивительных животных! 💚
Проверь свою интуицию и узнавай, какое животное в зоопарке тебе ближе всего. Задай себе пару важных вопросов: — Где бы ты хотел жить? — Какая еда тебе по душе? 🍽️
Нажми кнопку ниже, чтобы начать викторину и пройти путь к своему тотемному животному! 🦓""",
        reply_markup=markup
    )
    
    
@bot.callback_query_handler(func=lambda call: call.data == "start_quiz")
def start_quiz(call):
    user_data[call.message.chat.id]["current_question"] = 0
    user_data[call.message.chat.id]["score"] = {}
    send_question(call.message.chat.id)


def send_question(chat_id):
    current_question_index = user_data[chat_id]["current_question"]

    if current_question_index < len(QUESTIONS):
        question = QUESTIONS[current_question_index]
        text = question["text"]
        answers = question["answers"]
        image = question["img"]

        markup = InlineKeyboardMarkup()

        for i, answer in enumerate(answers):
            callback_data = f"answer:{current_question_index}:{i}" 
            markup.add(InlineKeyboardButton(answer["text"], callback_data=callback_data))
        
        bot.send_photo(chat_id, image, text, reply_markup=markup)
    
    else:
        send_result(chat_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("answer:"))
def handle_answer(call):
    data = call.data.split(":")
    current_question_index = int(data[1])
    answer_index = int(data[2])

    answer = QUESTIONS[current_question_index]["answers"][answer_index]
    chat_id = call.message.chat.id

    for animal, points in answer["points"].items():
        user_data[chat_id]["score"][animal] = user_data[chat_id]["score"].get(animal, 0) + points

    user_data[chat_id]["current_question"] += 1
    send_question(chat_id)


def send_result(chat_id):
    score = user_data[chat_id]["score"]
    animal = max(score, key=score.get) 
    result = RESULTS[animal]

    bot.send_photo(chat_id, result["image"], caption=f"{result['description']}")

bot.polling(none_stop=True)
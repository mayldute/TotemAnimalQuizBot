import telebot
from config import TOKEN, ADMIN_ID, QUESTIONS, RESULTS
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading
import time
from extensions import handle_redis_connection_error, handle_image_caching_error, handle_user_data_error, handle_general_error

bot = telebot.TeleBot(TOKEN)

user_data = {}

USER_DATA_LIFETIME = 86400  

def clear_inactive_users():
    """Функция для очистки данных неактивных пользователей."""
    while True:
        current_time = time.time()
        inactive_users = []
        
        for user_id, data in list(user_data.items()):
            last_interaction_time = data.get("last_interaction", 0)
            
            if current_time - last_interaction_time > USER_DATA_LIFETIME:
                inactive_users.append(user_id)
        
        for user_id in inactive_users:
            del user_data[user_id]
        
        time.sleep(3600) 

cleanup_thread = threading.Thread(target=clear_inactive_users, daemon=True)
cleanup_thread.start()

r = handle_redis_connection_error()

def cache_image_with_redis(image_url):
    """Кэширование изображений с Redis."""
    if r is None:
        return None  

    cached_image = r.get(image_url)
    
    if cached_image:
        return cached_image
    else:
        image_data = handle_image_caching_error(image_url)
        if image_data:
            r.setex(image_url, 3600, image_data) 
        return image_data


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Функция приветствия."""
    markup = InlineKeyboardMarkup()
    start_button = InlineKeyboardButton("Начать викторину", callback_data="start_quiz")
    guardianship = InlineKeyboardButton("О программе опекунства", url="https://moscowzoo.ru/about/guardianship")

    markup.add(start_button)
    markup.add(guardianship)

    user_data[message.chat.id] = {"score": {}, "current_question": 0, "last_interaction": time.time()}
    bot.send_message(
        message.chat.id,
        """Привет! 
Добро пожаловать в увлекательную викторину, где ты узнаешь, какое тотемное животное скрывается внутри тебя! 🐾
Московский зоопарк приглашает тебя на это забавное и познавательное путешествие по миру животных. В процессе викторины ты познакомишься с интересными фактами и уникальными особенностями обитателей нашего зоопарка. 
А ещё — возможно, ты станешь опекуном одного из этих удивительных животных! 
Проверь свою интуицию и узнавай, какое животное в зоопарке тебе ближе всего. Задай себе пару важных вопросов: — Где бы ты хотел жить? — Какая еда тебе по душе? 
Нажми кнопку ниже, чтобы начать викторину и пройти путь к своему тотемному животному! """,
        reply_markup=markup
    )
    
    
@bot.callback_query_handler(func=lambda call: call.data == "start_quiz")
def start_quiz(call):
    """Функция начала викторины."""
    user_data[call.message.chat.id]["current_question"] = 0
    user_data[call.message.chat.id]["score"] = {}
    send_question(call.message.chat.id)


def send_question(chat_id):
    """Функция для проверки наличия вопросов и отправки следующего вопроса или результата."""
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
    """Функция обработки ответов."""
    data = call.data.split(":")
    current_question_index = int(data[1])
    answer_index = int(data[2])

    answer = QUESTIONS[current_question_index]["answers"][answer_index]
    chat_id = call.message.chat.id

    for animal, points in answer["points"].items():
        user_data[chat_id]["score"][animal] = user_data[chat_id]["score"].get(animal, 0) + points

    user_data[chat_id]["current_question"] += 1
    send_question(chat_id)

def create_result_buttons():
    """Функция создания кнопок для сообщения с результатом."""
    markup = InlineKeyboardMarkup()
    guardianship = InlineKeyboardButton("Стать опекуном", url="https://moscowzoo.ru/about/guardianship")
    restart_button = InlineKeyboardButton("Повторить попытку?", callback_data="start_quiz")
    contact_support = InlineKeyboardButton("Связаться с сотрудником", callback_data="contact_support")
    share_button = InlineKeyboardButton("📢 Поделиться", callback_data="share_menu")
    feedback_button = InlineKeyboardButton("Оставить отзыв", callback_data="leave_feedback")

    markup.add(restart_button)
    markup.add(guardianship, share_button)
    markup.add(feedback_button, contact_support)
    
    
    return markup

def create_back_button():
    """Функция создания кнопки возврата на сообщение с результатом."""
    markup = InlineKeyboardMarkup()
    back_button = InlineKeyboardButton("🔙 Вернуться", callback_data="back_to_result")
    markup.add(back_button)

    return markup

def send_result(chat_id):
    """Функция отправки результата."""
    score = user_data[chat_id]["score"]
    animal = max(score, key=score.get) 
    result = RESULTS[animal]

    markup = create_result_buttons()

    text = f"{result['description']}\n\n[Узнай больше...]({result['url']})"

    bot.send_photo(chat_id, result["image"], caption=text, reply_markup=markup, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data == "contact_support")
def contact_support(call):
    """Функция запроса информации у пользователя."""
    chat_id = call.message.chat.id
    bot.send_message(chat_id, "Напишите ваш вопрос, и мы свяжемся с вами как можно скорее.")
    bot.register_next_step_handler_by_chat_id(chat_id, forward_to_admin)

def forward_to_admin(message):
    """Функция отправки информации админу."""
    chat_id = message.chat.id
    user_question = message.text

    user_result = user_data.get(chat_id, {}).get("score", {})
    result_text = "\n".join([f"{animal}: {points}" for animal, points in user_result.items()])
    
    admin_message = f"📩 Новый запрос от пользователя: @{message.from_user.username}\n\n"
    admin_message += f"🔍 Результат викторины:\n{result_text}\n\n"
    admin_message += f"💬 Вопрос пользователя: {user_question}"

    bot.send_message(ADMIN_ID, admin_message)

    markup = create_back_button()

    bot.send_message(chat_id, "Ваш вопрос отправлен сотруднику. Ожидайте ответа!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "leave_feedback")
def ask_feedback(call):
    """Функция запроса отзыва."""
    chat_id = call.message.chat.id
    bot.send_message(chat_id, "Напишите ваш отзыв о боте или викторине:")
    bot.register_next_step_handler_by_chat_id(chat_id, forward_feedback_to_admin)


def forward_feedback_to_admin(message):
    """Функция отправки отзыва админу."""
    chat_id = message.chat.id
    feedback_text = message.text

    admin_message = f"📝 Новый отзыв от @{message.from_user.username}:\n\n{feedback_text}"
    bot.send_message(ADMIN_ID, admin_message)

    markup = create_back_button()

    bot.send_message(chat_id, "Спасибо за ваш отзыв! Он поможет нам стать лучше. 😊", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "share_menu")
def share_menu(call):
    """Функция выбора соцсети для отправки результата."""
    chat_id = call.message.chat.id
    score = user_data[chat_id]["score"]
    animal = max(score, key=score.get) 
    
    result_text = f"📢 Я прошёл викторину и узнал своё тотемное животное - {animal}! 🐾\n\nПройди тест и узнай своё: https://t.me/YourBotUsername"
    
    markup = InlineKeyboardMarkup()
    
    twitter = InlineKeyboardButton("🐦 Twitter", url=f"https://twitter.com/intent/tweet?text={result_text}")
    vk = InlineKeyboardButton("📘 ВКонтакте", url=f"https://vk.com/share.php?url=https://t.me/TotemAnimalQuizBot")
    facebook = InlineKeyboardButton("📘 Facebook", url=f"https://www.facebook.com/sharer/sharer.php?u=https://t.me/TotemAnimalQuizBot")
    telegram = InlineKeyboardButton("✈️ Telegram", switch_inline_query=result_text)
    back_button = InlineKeyboardButton("🔙 Вернуться", callback_data="back_to_result")
    
    markup.add(twitter, vk)
    markup.add(facebook, telegram)
    markup.add(back_button)

    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "back_to_result")
def back_to_result(call):
    """Функция возврата к сообщению с результатом."""
    chat_id = call.message.chat.id
    user_score = user_data.get(chat_id, {}).get("score", {})
    
    animal = max(user_score, key=user_score.get)
    result = RESULTS[animal]
    
    markup = create_result_buttons()

    if call.message.caption:
        markup = create_result_buttons()
        bot.edit_message_caption(
            chat_id=chat_id,
            message_id=call.message.message_id,
            caption=f"{result['description']}\n\n[Узнай больше...]({result['url']})",
            reply_markup=markup,
            parse_mode="Markdown"
        )
    else:
        markup = create_result_buttons()
        bot.send_photo(
            chat_id,
            result["image"],
            caption=f"{result['description']}\n\n[Узнай больше...]({result['url']})",
            reply_markup=markup,
            parse_mode="Markdown"
        )


bot.polling(none_stop=True)
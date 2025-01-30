@TotemAnimalQuizBot is an interactive Telegram quiz bot designed to promote the Moscow Zoo’s adoption program. It helps users discover their "totem animal" and learn more about how they can become a guardian of one of the zoo's animals.

**Functionality:**
Easy Interaction – The bot starts with the /start command or a button. It guides the user through the entire quiz process by asking multiple-choice questions.\n
Interactive Quiz – Sequential questions with images help determine the user’s totem animal.

Answer Processing Algorithm – Each answer is assigned points, which ultimately determine the result.

Result Generation – At the end of the quiz, the bot sends the user a description of their totem animal and a link to the adoption program.

Image Support – The quiz is accompanied by images, and the result includes an image of the specific animal.

Social Media Integration – The user can easily share the result via Twitter, VK, Facebook, and Telegram.

Zoo Staff Contact – Users can send a question to a zoo staff member, with the quiz result included.

Quiz Restart – The bot allows the user to retake the quiz.

Feedback Collection – Users can leave feedback about the bot and the quiz.

Security and Privacy – User data is stored for no more than 24 hours, in compliance with GDPR.

Scalability – The bot works reliably as the number of users increases.

Optimization and Monitoring – Multitasking and error handling are used, such as Redis for image caching.

Requirements:
Python 3.8+
Libraries from requirements.txt:
pip install -r requirements.txt

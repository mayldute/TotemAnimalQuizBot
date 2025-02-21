# Moscow Zoo Totem Animal Quiz Bot

This project is a Telegram bot that offers users an interactive quiz to discover their totem animal based on their preferences and personality. Built using python-telegram-bot, Redis, and threading, it also allows users to share results, contact support, and leave feedback.

## Features
- Interactive Quiz: Answer fun questions to find your totem animal.
- Personalized Results: Each result comes with a detailed animal description and image.
- Guardianship Program Info: Direct links to become an animal guardian.
- Feedback and Support: Users can send feedback or contact support.
- Retake Quiz: Allows users to retake the quiz anytime.
- Sharing Options: Share your results on social media platforms.

## Technologies Used
- Python – The main programming language.
- PyTelegramBotAPI – For interacting with Telegram’s Bot API.
- Redis – Caching images to improve performance.
- Threading – Manages inactive user data cleanup.
- dotenv – Securely handles environment variables.

## Setup and Installation

1. Clone the Repository
```bash
git clone https://github.com/yourusername/totemanimalquiz.git
cd totemanimalquiz
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Configure Environment Variables
Create a `.env` file and set your token and admin ID:
```bash
TOKEN=your_telegram_bot_token
ADMIN_ID=your_telegram_user_id
```

4. Set Up Redis

Make sure Redis is installed and running:
```bash
sudo apt update
sudo apt install redis-server
sudo systemctl start redis
sudo systemctl enable redis
```

## How to Run the Bot
```bash
python bot.py
```
The bot will start polling and be available on Telegram.

## Usage Guide

### Start the Quiz
- Send `/start` to begin.
- Follow on-screen questions.
- Your totem animal result will be shown at the end.

### Contact Support
- Use the Contact Support button after receiving results to ask questions.

### Leave Feedback
- Share your thoughts using the Leave Feedback button.

### Share Results
- Share your quiz results directly on:
    - Twitter
    - VK
    - Facebook
    - Telegram

## Admin Features
- Receive user questions and feedback directly via Telegram.
- Track user results for insights.

## Error Handling
- Redis connection issues
- Image caching failures
- Missing or corrupted user data

All errors are logged and handled gracefully without affecting the user experience.

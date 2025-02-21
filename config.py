import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

QUESTIONS = [
    {
        "text": "Where would you like to live?",
        "answers": [
            {"text": "In the forest", "points": {"East Siberian Lynx": 3, "Snow Leopard": 2}},
            {"text": "In the steppe", "points": {"Grevy's Zebra": 3}},
            {"text": "By the river", "points": {"European Otter": 2, "Mute Swan": 3}},
            {"text": "In the mountains", "points": {"Snow Leopard": 3}}
        ],
        "img": "https://i.pinimg.com/474x/ac/b3/35/acb335a3a3fc4e6a2da1f6cd9cc37db7.jpg",
    },
    {
        "text": "What is your favorite food?",
        "answers": [
            {"text": "Fruits and vegetables", "points": {"Grevy's Zebra": 2, "European Otter": 3}},
            {"text": "Fish", "points": {"European Otter": 3}},
            {"text": "Meat", "points": {"East Siberian Lynx": 3, "Snow Leopard": 2}},
            {"text": "Grain", "points": {"Mute Swan": 3}}
        ],
        "img": "https://i.pinimg.com/474x/14/b4/5b/14b45b1b8880986cb36628ec37594f00.jpg",
    },
    {
        "text": "How do you prefer to spend your free time?",
        "answers": [
            {"text": "In peace and reflection", "points": {"Mute Swan": 3}},
            {"text": "Playing active games", "points": {"European Otter": 2, "Grevy's Zebra": 3}},
            {"text": "Exploring nature", "points": {"Snow Leopard": 3, "East Siberian Lynx": 2}},
            {"text": "In a comfort zone", "points": {"African Penguin": 3}}
        ],
        "img": "https://i.pinimg.com/736x/16/7c/1e/167c1e9b4b981fcdbdf48219da3b8933.jpg",
    },
    {
        "text": "What is your personality like?",
        "answers": [
            {"text": "Patient and caring", "points": {"Amur Tiger": 3}},
            {"text": "Energetic and curious", "points": {"European Otter": 2, "Grevy's Zebra": 3}},
            {"text": "Independent and a bit mysterious", "points": {"East Siberian Lynx": 3, "Snow Leopard": 2}},
            {"text": "Calm and majestic", "points": {"Mute Swan": 3}}
        ],
        "img": "https://i.pinimg.com/736x/5c/ac/5a/5cac5a9ca9ea765671b446a7480f09f9.jpg",
    },
    {
        "text": "How do you feel about company?",
        "answers": [
            {"text": "I prefer to be alone", "points": {"Amur Tiger": 3}},
            {"text": "I like company, but not always", "points": {"Snow Leopard": 2}},
            {"text": "I love being surrounded by others", "points": {"European Otter": 3, "Grevy's Zebra": 2}},
            {"text": "I’m always with friends and family", "points": {"African Penguin": 3}}
        ],
        "img": "https://i.pinimg.com/736x/2a/a3/21/2aa3219150c693f022adc0e5dda06ef7.jpg",
    },
    {
        "text": "What lifestyle suits you best?",
        "answers": [
            {"text": "I love traveling and exploring", "points": {"Snow Leopard": 3, "Amur Tiger": 2}},
            {"text": "I prefer to relax at home", "points": {"African Penguin": 2, "Mute Swan": 3}},
            {"text": "I enjoy active hobbies", "points": {"European Otter": 3, "Grevy's Zebra": 2}},
            {"text": "I always find time for myself", "points": {"Amur Leopard": 3}}
        ],
        "img": "https://i.pinimg.com/474x/d5/f2/42/d5f24202a391168ab2f52220f92da7f8.jpg",
    },
    {
        "text": "How do you feel about cold weather?",
        "answers": [
            {"text": "I like the cold, I feel comfortable in frost", "points": {"African Penguin": 3, "Snow Leopard": 2}},
            {"text": "Cold isn’t for me, I prefer warmth", "points": {"European Otter": 2, "Amur Leopard": 3}},
            {"text": "I can adapt to any weather", "points": {"Grevy's Zebra": 3}},
            {"text": "I prefer moderate conditions", "points": {"Amur Tiger": 3, "Mute Swan": 2}}
        ],
        "img": "https://i.pinimg.com/474x/fa/60/9e/fa609ef81a8ee80bf6516eed87324b3a.jpg",
    },
]

RESULTS = {
    "East Siberian Lynx": {
        "description": "You are an East Siberian Lynx! Independent and secretive. You love solitude, and your grace and strength impress those around you. You always know exactly what you want and never give up despite difficulties. You can be found in the wild taiga, where you are a true master of stealth.",
        "image": "https://i.pinimg.com/474x/39/84/bc/3984bce43f624988048b03fc5b8ddb10.jpg",
        "url": "https://moscowzoo.ru/animals/kinds/vostochno_sibirskaya_rys"
    },
    "Snow Leopard": {
        "description": "You are a Snow Leopard! A free-spirited explorer. You possess bravery and a free spirit, always striving for new heights. You prefer solitude and dislike being confined. Your majestic walk and survival skills in the harshest conditions command admiration.",
        "image": "https://i.pinimg.com/474x/95/cd/e0/95cde05f94637d018e1874e985281441.jpg",
        "url": "https://moscowzoo.ru/animals/kinds/irbis_snezhnyy_bars"
    },
    "Grevy's Zebra": {
        "description": "You are Grevy's Zebra! Energetic and friendly. You love being the center of attention, and your unique stripes delight everyone. Your quick reactions and adaptability make you a great companion for any adventure.",
        "image": "https://i.pinimg.com/474x/28/58/29/285829f5368356af685e75fe8a67debf.jpg",
        "url": "https://moscowzoo.ru/animals/kinds/zebra_grevi"
    },
    "European Otter": {
        "description": "You are a European Otter! Curious and playful. You’re always seeking new experiences and love having fun. Your genuine joy and friendliness can cheer anyone up. You’re always looking for adventure, whether in water or on land.",
        "image": "https://i.pinimg.com/474x/96/2a/4d/962a4d60cbb4ed2e5e0c6ff81a7d909a.jpg",
        "url": "https://moscowzoo.ru/animals/kinds/obyknovennaya_vydra"
    },
    "Mute Swan": {
        "description": "You are a Mute Swan! Calm and majestic. You enjoy harmony and the beauty around you. You always remain reserved, but hidden within you is true strength. You are a symbol of grace and elegance, and your presence makes people reflect on the grandeur of nature.",
        "image": "https://i.pinimg.com/474x/5b/9d/85/5b9d85394d391ed3f17e38c2bdf5ecd2.jpg",
        "url": "https://moscowzoo.ru/animals/kinds/lebed_shipun"
    },
    "Amur Tiger": {
        "description": "You are an Amur Tiger! Powerful and brave. You embody strength and confidence. Every step you take is calculated, and you always achieve your goals. You’re a lone wolf but capable of being a loyal friend. Your determination and intellect allow you to overcome any obstacle on the road to success.",
        "image": "https://i.pinimg.com/474x/20/a2/30/20a230452438e019fcb159ee08592cb9.jpg",
        "url": "https://moscowzoo.ru/animals/kinds/amurskiy_tigr"
    },
    "African Penguin": {
        "description": "You are a Penguin! Funny and resilient. You always stay optimistic and know how to find joy in simple things. Your resilience and unwavering spirit help you overcome any difficulties. You always work as a team and value your group. It's always fun and warm with you around.",
        "image": "https://i.pinimg.com/474x/5d/06/ae/5d06aefb04b6cfe94790dea743274ca7.jpg",
        "url": "https://moscowzoo.ru/animals/kinds/pingvin_afrikanskiy_ochkovyy"
    },
    "Amur Leopard": {
        "description": "You are a Leopard! Quiet and strong. You always act with precision and gracefully overcome any challenge. Your confidence and calmness help you find a way out of even the most difficult situations. You prefer to stay in the shadows, but your strength and hunting skills command admiration.",
        "image": "https://i.pinimg.com/474x/70/c9/f7/70c9f722a23843af40324d74a847dc5d.jpg",
        "url": "https://moscowzoo.ru/animals/kinds/dalnevostochnyy_leopard"
    }
}

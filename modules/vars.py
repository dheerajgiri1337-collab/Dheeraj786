#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "39855240"))
API_HASH = environ.get("API_HASH", "a17c43755159b1e8fc0ea5120d00675f")
BOT_TOKEN = environ.get("BOT_TOKEN", "8725871722:AAHW_WnaHHRF5tW4XCYM5e3cJ9ywmmtBv8M")

OWNER = int(environ.get("OWNER", "7068785548"))
CREDIT = environ.get("CREDIT", "𝕯𝖍𝖊𝖊𝖗𝖆𝖏_𝕭𝖔𝖙𝖘")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7068785548').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7068785548').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

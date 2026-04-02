import os, sys, asyncio, requests
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, InputMediaPhoto

# Variable Imports
from vars import API_ID, API_HASH, BOT_TOKEN, OWNER, CREDIT, AUTH_USERS, TOTAL_USERS
import globals

# Handler Imports
from html_handler import register_html_handlers
from drm_handler import register_drm_handlers
from text_handler import register_text_handlers
from features import register_feature_handlers
from upgrade import register_upgrade_handlers
from commands import register_commands_handlers
from settings import register_settings_handlers
from broadcast import register_broadcast_handlers
from youtube_handler import register_youtube_handlers
from authorisation import register_authorisation_handlers

# Initialize the bot
bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Main Keyboard
keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🎙️ Commands", callback_data="cmd_command")],
    [InlineKeyboardButton("💎 Features", callback_data="feat_command"), InlineKeyboardButton("⚙️ Settings", callback_data="setttings")],
    [InlineKeyboardButton("💳 Subscription", callback_data="upgrade_command")],
    [InlineKeyboardButton(text="📞 Contact", url=f"tg://openmessage?user_id={OWNER}"), InlineKeyboardButton(text="🛠️ Repo", url="https://github.com/nikhilsainiop/saini-txt-direct")],
])      

@bot.on_message(filters.command("start"))
async def start(bot, m: Message):
    user_id = m.chat.id
    if user_id not in TOTAL_USERS:
        TOTAL_USERS.append(user_id)
    
    # Yahan branding "Dheeraj Bots" kar di hai
    caption = (
        f"𝐇𝐞𝐥𝐥𝐨 **{m.from_user.first_name}** 👋!\n\n"
        f"➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭\n"
        f"➠ Can Extract Videos & PDFs From Your Text File!\n\n"
        f"➠ 𝐌𝐚𝐝𝐞 𝐁𝐲 : [𝐃𝐡𝐞𝐞𝐫𝐚𝐣 𝐁𝐨𝐭𝐬](tg://openmessage?user_id={OWNER}) 🦁"
    )
    
    await bot.send_photo(
        chat_id=m.chat.id,
        photo="https://iili.io/KuCBoV2.jpg", # Dinner ke baad ise change karenge
        caption=caption,
        reply_markup=keyboard
    )

# Sare Handlers Register Karo
register_text_handlers(bot)
register_html_handlers(bot)
register_feature_handlers(bot)
register_settings_handlers(bot)
register_upgrade_handlers(bot)
register_commands_handlers(bot)
register_broadcast_handlers(bot)
register_youtube_handlers(bot)
register_authorisation_handlers(bot)
register_drm_handlers(bot)

def notify_owner():
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": OWNER, "text": "𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐨𝐧 𝐑𝐞𝐧𝐝𝐞𝐫 (𝐖𝐨𝐫𝐤𝐞𝐫) ✅"})
    except: pass

if __name__ == "__main__":
    notify_owner()
    print("Bot is running as a Background Worker...")
    bot.run()

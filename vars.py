import os
from os import environ

# API Configuration
API_ID = int(os.environ.get("API_ID", "27765349"))
API_HASH = os.environ.get("API_HASH", "9df1f705c8047ac0d723b29069a1332b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

CREDIT = os.environ.get("CREDIT", "Star AJ")
# MongoDB Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "UGxPRO")
DATABASE_URL = os.environ.get("DATABASE_URL", "")
MONGO_URL = DATABASE_URL  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "1116405290"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "1116405290").split()]  # Default to owner ID

# Channel Configuration
PREMIUM_CHANNEL = "https://t.me/+W-Q51EuLf2QwYTl"
# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "https://imgs.search.brave.com/THqPKczwvPZMcP7ME81cY86Y_zf3C5TvrUIkce6YNCo/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9yMi5z/dGFycnlhaS5jb20v/cmVzdWx0cy8xMDA3/MzQ3OTcwLzk2NzVj/YjQzLWE4YmEtNGYy/Ny05NmU5LTYzYTNk/NzVlYTQ5Zi53ZWJw").split()))

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>\n\n Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name: {name}
🆔 User ID: {user_id}
📅 Expiry: {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully!</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin @ItsUGBot to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}


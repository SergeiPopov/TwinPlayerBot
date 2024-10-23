import os
import asyncio

import environ
from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


async def main():
    env = environ.Env()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    TG_TOKEN = env('TG_TOKEN')

    """Start the Bot."""
    # Create the Application and pass it your Bot's token.
    application = Application.builder().token("TOKEN").build()

    # Keep track of which chats the Bot is in
    application.add_handler(ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER))
    application.add_handler(CommandHandler("show_chats", show_chats))

    # Handle members joining/leaving chats.
    application.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))

    # Interpret any other command or text message as a start of a private chat.
    # This will record the user as being in a private chat with Bot.
    application.add_handler(MessageHandler(filters.ALL, start_private_chat))

    # Run the Bot until the user presses Ctrl-C
    # We pass 'allowed_updates' handle *all* updates including `chat_member` updates
    # To reset this, simply pass `allowed_updates=[]`
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    asyncio.run(main())
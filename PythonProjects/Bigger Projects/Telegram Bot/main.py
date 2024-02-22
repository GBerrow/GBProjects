"""This Python script sets up a Telegram bot using the python-telegram-bot library.
The bot listens for messages from users and responds based on predefined commands and custom response logic.
It includes handlers for commands like /start, /help, and /custom,
as well as a message handler to respond to any text message received.
The bot provides basic conversational responses based on the content of the messages received,
such as greeting users, responding to inquiries about its well-being,
and acknowledging users' expressions of affection for Python programming language.
The script also includes error handling to log and handle any errors that occur during bot operation.
Overall this code provides a basic framework for building a Telegram bot,
capable of engaging in simple conversational interactions with users.
"""


from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# pip install python-telegram-bot

TOKEN: Final[str] = 'YOUR_BOT_TOKEN_HERE'
BOT_USERNAME: Final[str] = '@your_bot_username'


# Custom responses based on user input
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I am good, thanks! How about you?'

    if 'i love python' in processed:
        return 'Python is cool!'

    return 'I do not understand... Please try asking something else.'


# Handle commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""
    await update.message.reply_text('Hello there! Nice to meet you. Let\'s chat!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command."""
    await update.message.reply_text('Just type something and I will respond to you!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /custom command."""
    await update.message.reply_text('This is a custom command.')


# Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages."""
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Log users
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # Handle message type
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    # Reply
    print('Bot:', response)
    await update.message.reply_text(response)


# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors."""
    print(f'Update {update} caused error: {context.error}')


def main():
    """Main function."""
    print('Starting up bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Define a poll interval
    print('Polling...')
    app.run_polling(poll_interval=5)


if __name__ == '__main__':
    main()

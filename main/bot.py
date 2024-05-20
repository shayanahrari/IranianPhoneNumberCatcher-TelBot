from telegram import Bot
from telegram import __version__ as TG_VER
from main.tools import extract_phone_numbers, save_numbers, count_numbers, save_error_numbers, extract_tags
from settings.config import (
    TOKEN_BOT,
)
from telegram import (
    Update,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackContext,
    DictPersistence,
)
from warnings import filterwarnings
from telegram.warnings import PTBUserWarning
from settings.log_conf import logger
from colorama import Fore, Style, init

filterwarnings(
    action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning
)


try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)
if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )


# Enable logging
init(autoreset=True)
logger.info(f"{Fore.GREEN}BOT IS ON ......{Style.RESET_ALL}")


bot = Bot(token=TOKEN_BOT)


# Define the start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Hi! Send me any text, and I will extract Phone numbers and save them ;)."
    )


# Define the message handler
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.caption

    if text is None:
        text = update.message.text

    try:
        numbers_list = extract_phone_numbers(text)
        tags_list = extract_tags(text)

        if numbers_list:
            save_numbers(numbers_list, tags=tags_list, set_tag=True)
            save_numbers(numbers_list, tags=tags_list, set_tag=False)
            numbers_count = count_numbers('numbers.txt')

            await update.message.reply_text(f'✅Numbers extracted and saved. count:{str(numbers_count)}')
        else:
            save_error_numbers(text)
            await update.message.reply_text("❌No numbers found in the text❌")

    except Exception as e:
        logger.error(e)
        pass


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error('the error handler find an error', exc_info=context.error)
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id=chat_id,
        text='an error was occured please wait for the start menu....'
    )
    await start(update, context)


def main():
    """Run the bot."""
    persistence = DictPersistence()
    application = Application.builder().token(TOKEN_BOT).persistence(persistence).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, handle_message))
    application.add_error_handler(error_handler)
    filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

    # nest_asyncio.apply()
    application.run_polling(allowed_updates=Update.ALL_TYPES)



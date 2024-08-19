from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Вставьте сюда свой токен
TOKEN = '7320968761:AAHds8vvVlqRwJH8ZR5-ZGC1zAjGTnnovaI'

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(f'Вы сказали: {text}')

def main() -> None:
    # Создаем экземпляр Application
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('info', info_command))

    # Добавляем обработчик для текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()

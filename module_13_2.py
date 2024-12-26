
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# Указываем токен бота
API_TOKEN = '123456789'

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    print("Привет! Я бот помогающий твоему здоровью.")  # Вывод в консоль
    await message.reply("Привет! Я бот помогающий твоему здоровью.")  # Ответ пользователю

# Обработчик всех остальных сообщений
@dp.message_handler()
async def all_messages(message: Message):
    print("Введите команду /start, чтобы начать общение.")  # Вывод в консоль
    await message.reply("Введите команду /start, чтобы начать общение.")  # Ответ пользователю

# Запуск бота
if __name__ == '__main__':
    print("бот работает")
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
API_TOKEN = '123'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Привет! Я бот, помогающий вашему здоровью.")


@router.message()
async def all_messages(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать общение с ботом"),
    ]
    await bot.set_my_commands(commands)

async def main():
    try:
        print("Бот пашет...")
        await set_commands(bot)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())

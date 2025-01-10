import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

API_TOKEN = '123'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    logger.info("Команда /start")
    await message.answer("Привет! Я бот, помогающий твоему здоровью.\nНапишите 'Calories', чтобы начать.")

@router.message(lambda message: message.text.lower() == "calories")
async def set_age(message: Message, state: FSMContext):
    logger.info("Получено 'Calories'")
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    logger.info("Ввод возраста")
    try:
        age = int(message.text)
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом.")
        await state.update_data(age=age)
        await message.answer("Введите свой рост (в см):")
        await state.set_state(UserState.growth)
    except ValueError:
        await message.answer("Введите корректный возраст (число).")

@router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    logger.info("Введите рост")
    try:
        growth = int(message.text)
        if growth <= 0:
            raise ValueError("Рост должен быть положительным числом.")
        await state.update_data(growth=growth)
        await message.answer("Введите вес (в кг):")
        await state.set_state(UserState.weight)
    except ValueError:
        await message.answer("Введите корректный рост в сантиметрах.")

@router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    logger.info("Ввод веса")
    try:
        weight = int(message.text)
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        await state.update_data(weight=weight)

        data = await state.get_data()
        age, growth, weight = data['age'], data['growth'], data['weight']

        calories = 10 * weight + 6.25 * growth - 5 * age - 161

        await message.answer(
            f"Ваши данные:\nВозраст: {age} лет\nРост: {growth} см\nВес: {weight} кг\n"
            f"Норма калорий: {calories:.2f} ккал в день."
        )
        await state.clear()
    except ValueError:
        await message.answer("Введите корректный вес (число).")

async def main():
    logger.info("Бот пашет как проклятый")
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

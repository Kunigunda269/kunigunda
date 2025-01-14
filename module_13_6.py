from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

API_TOKEN = '123'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

class Form(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")],
    ]
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
            InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
        ]
    ]
)


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью.",
        reply_markup=keyboard
    )


@router.message(lambda msg: msg.text == "Рассчитать")
async def main_menu(message: Message):
    await message.answer(
        "Выберите опцию:",
        reply_markup=inline_keyboard
    )


@router.callback_query(lambda call: call.data == "formulas")
async def get_formulas(call: CallbackQuery):
    formula = "10 × вес (кг) + 6.25 × рост (см) − 5 × возраст (г) − 161"
    await call.message.answer(f"Формула Миффлина-Сан Жеора:\n{formula}")
    await call.answer()


@router.callback_query(lambda call: call.data == "calories")
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст:")
    await state.set_state(Form.age)
    await call.answer()


@router.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await state.set_state(Form.growth)


@router.message(Form.growth)
async def process_growth(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await state.set_state(Form.weight)


@router.message(Form.weight)
async def process_weight(message: Message, state: FSMContext):
    data = await state.get_data()
    age = int(data["age"])
    growth = int(data["growth"])
    weight = int(message.text)

    bmr = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша норма калорий: {bmr:.2f}")
    await state.clear()



async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

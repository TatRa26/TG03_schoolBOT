from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.database import save_student

# Определение машины состояний
class Registration(StatesGroup):
    name = State()
    age = State()
    grade = State()

# Создаем роутер
router = Router()

# Хэндлер для команды /start
@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет! Давай начнем регистрацию. Как тебя зовут?")
    await state.set_state(Registration.name)

# Обработчик имени
@router.message(Registration.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(Registration.age)

# Обработчик возраста
@router.message(Registration.age, F.text.isdigit())
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer("В каком ты классе?")
    await state.set_state(Registration.grade)

@router.message(Registration.age)
async def process_age_invalid(message: Message):
    await message.answer("Пожалуйста, введи свой возраст числом.")

# Обработчик класса
@router.message(Registration.grade)
async def process_grade(message: Message, state: FSMContext):
    user_data = await state.get_data()
    save_student(user_data['name'], user_data['age'], message.text)
    await message.answer("Спасибо! Твои данные сохранены.")
    await state.clear()


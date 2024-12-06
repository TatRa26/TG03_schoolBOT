import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers import router
from bot.database import init_db
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Проверка наличия токена бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Токен бота не найден в .env файле")

# Создание экземпляров бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    """Основная функция для запуска бота."""
    # Инициализация базы данных
    init_db()

    # Регистрация маршрутов
    dp.include_router(router)

    # Логгирование
    logger.info("Бот успешно запущен")

    # Запуск long-polling
    await dp.start_polling(bot)

# Точка входа в программу
if __name__ == "__main__":
    asyncio.run(main())




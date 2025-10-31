import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from fastapi import FastAPI
from fastapi.responses import FileResponse
import threading
import uvicorn

TOKEN = "7847350031:AAEQ_zS5ogg7KLIy8crM9UpHqGAlllQj0RI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# FastAPI сервер
app = FastAPI()

@app.get("/")
async def index():
    return FileResponse("web/index.html")

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text="Открыть приложение 🌸",
                web_app=types.WebAppInfo(url="https://radhe-radhe-bot.onrender.com")
            )]
        ]
    )
    await message.answer("Харе Кришна! Нажми кнопку, чтобы открыть приложение:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

def start_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    threading.Thread(target=start_fastapi).start()
    asyncio.run(main())

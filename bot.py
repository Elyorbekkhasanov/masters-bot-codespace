import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import sqlite3

# ================= CONFIG =================
BOT_TOKEN = "7828918931:AAGTLhiDoyCH7QNbWQNiJvDmSaxMLTtU0yU"
ADMIN_ID = 7738180710
TELEGRAM_CHANNEL = "https://t.me/masters_qurilish"
INSTAGRAM_LINK = "https://instagram.com/masters_qurilish"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ================= DATABASE =================
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('masters.db')
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT,
                phone TEXT,
                registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

db = Database()

# ================= KEYBOARDS =================
def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📅 Barakotli Juma"), KeyboardButton(text="🎯 11.11 Aksiyasi")],
            [KeyboardButton(text="🔥 Chegirmalar"), KeyboardButton(text="👤 Mening ma'lumotlarim")],
            [KeyboardButton(text="🏢 Biz haqimizda"), KeyboardButton(text="📞 Bog'lanish")]
        ],
        resize_keyboard=True
    )

# ================= HANDLERS =================
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "🤖 <b>Master`s Santexnika va Qurilish Mollari</b>\n\n"
        "Xush kelibsiz! Aksiyalarimizda ishtirok eting va yutuqlarga ega bo'ling!",
        reply_markup=main_kb(),
        parse_mode="HTML"
    )

@dp.message(Command("test"))
async def test_cmd(message: types.Message):
    await message.answer("✅ <b>Bot ishlayapti!</b>", parse_mode="HTML")

@dp.message(F.text == "🔥 Chegirmalar")
async def discounts_btn(message: types.Message):
    text = """
🔥 <b>Chegirmadagi Mahsulotlar</b>

🛍️ <b>Armatura to'plami</b>
💰 <s>150,000 so'm</s> → <b>120,000 so'm</b>
📉 <b>20% CHEGIRMA</b>

🛍️ <b>Smart sanitarka</b>
💰 <s>280,000 so'm</s> → <b>220,000 so'm</b>
📉 <b>21% CHEGIRMA</b>

📍 <b>Buyurtma:</b> +998 XX XXX XX XX
"""
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "🏢 Biz haqimizda")
async def about_btn(message: types.Message):
    text = f"""
🏢 <b>Master`s Santexnika va Qurilish Mollari</b>

10 yillik tajriba bilan xizmat ko'rsatamiz!

📢 <b>Telegram:</b> {TELEGRAM_CHANNEL}
📷 <b>Instagram:</b> {INSTAGRAM_LINK}

🤝 <b>Biz ishonchli hamkormiz!</b>
"""
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "📞 Bog'lanish")
async def contact_btn(message: types.Message):
    text = """
📞 <b>Bog'lanish</b>

📍 Manzil: Shahar markazi
📱 Telefon: +998 XX XXX XX XX
🕒 Ish vaqti: 9:00 - 18:00

🚗 Yetkazib berish mavjud!
"""
    await message.answer(text, parse_mode="HTML")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(
        "Iltimos, quyidagi tugmalardan foydalaning:",
        reply_markup=main_kb()
    )

# ================= START BOT =================
async def main():
    print("🤖 Master`s Bot GitHub Codespaces da ishga tushmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

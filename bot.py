import random
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8109175665:AAGrinITZ3JUsteO_V0bBGcAiIRJ7FDCsx8"

import os
TOKEN = os.getenv("TOKEN")

answers = [
    "Да",
    "Нет",
    "Скорее всего",
    "Маловероятно",
    "Определённо да",
    "Спроси позже",
    "Не уверен",
    "Без сомнений",
    "Лучше не сейчас",
    "Звёзды говорят да"
]

async def eight_ball(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Напиши вопрос 😄\nПример:\n/8ball Я стану богатым?")
        return

    # Сообщение "думает"
    msg = await update.message.reply_text("🎱 Думаю...")

    # Задержка (имитация магии 😄)
    await asyncio.sleep(2)

    answer = random.choice(answers)

    # Редактируем сообщение (красивее чем новое)
    await msg.edit_text(f"🎱 {answer}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("8ball", eight_ball))

    print("Бот запущен...")
    app.run_polling()

import random
import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8109175665:AAGrinITZ3JUsteO_V0bBGcAiIRJ7FDCsx8")  # для Railway / хостинга

# Обычные ответы
normal_answers = [
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

# Саркастичные ответы
sarcastic_answers = [
    "О да, конечно... 🙄",
    "Ты серьёзно это спрашиваешь?",
    "Ну да, конечно, как же иначе 😏",
    "Нет. Даже не надейся.",
    "Спроси ещё что-нибудь глупее",
    "Я бы ответил, но мне лень",
    "Очевидно же... нет",
    "Ты правда хочешь это знать?",
]

# Легендарные ответы (1%)
legendary_answers = [
    "🌟 ТЫ ИЗБРАННЫЙ",
    "🔥 СЕГОДНЯ ТВОЙ ДЕНЬ",
    "💰 БОГАТСТВО УЖЕ РЯДОМ",
    "👑 ТЫ СТАНЕШЬ ЛЕГЕНДОЙ",
    "⚡ СУДЬБА НА ТВОЕЙ СТОРОНЕ"
]

# Режимы пользователей (чат_id: режим)
user_modes = {}

# Команда /8ball
async def eight_ball(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if not context.args:
        await update.message.reply_text(
            "Задай вопрос 😄\nПример:\n/8ball Я стану богатым?"
        )
        return

    msg = await update.message.reply_text("🎱 Думаю...")

    await asyncio.sleep(2)

    # 1% шанс легендарного ответа
    if random.randint(1, 100) == 1:
        answer = random.choice(legendary_answers)
    else:
        mode = user_modes.get(chat_id, "normal")

        if mode == "sarcastic":
            answer = random.choice(sarcastic_answers)
        else:
            answer = random.choice(normal_answers)

    await msg.edit_text(f"🎱 {answer}")

# Включить сарказм
async def sarcastic_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_modes[chat_id] = "sarcastic"
    await update.message.reply_text("🎭 Режим саркастичного шара ВКЛ")

# Выключить сарказм
async def sarcastic_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_modes[chat_id] = "normal"
    await update.message.reply_text("🎱 Обычный режим включен")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("8ball", eight_ball))
    app.add_handler(CommandHandler("sarcasm_on", sarcastic_on))
    app.add_handler(CommandHandler("sarcasm_off", sarcastic_off))

    print("Бот запущен...")
    app.run_polling()

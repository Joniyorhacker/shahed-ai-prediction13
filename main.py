import logging
import asyncio
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8380050511:AAHCU4h9lNDkQJMzU44kxE3Nx-Ujm6JTq2c"
REF_LINK = "https://dkwin9.com/#/register?invitationCode=16532572738"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

signal_running = False
current_chat_id = None
preyod_number = 20250816100010688  # starting market period
last_number = None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🤖 SHAHED AI PREDICTION BOT\n\n"
        f"🔹 Auto Wingo 1 Min Signals\n"
        f"🔹 Owner: @shahedbintarek\n"
        f"🔹 Join via link: {REF_LINK}\n\n"
        f"Commands:\n"
        f"/signal_on - Start auto signals in this group\n"
        f"/signal_off - Stop auto signals"
    )

async def signal_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global signal_running, current_chat_id
    signal_running = True
    current_chat_id = update.effective_chat.id
    await update.message.reply_text("✅ Auto Signal Started")
    asyncio.create_task(auto_signal(context))

async def signal_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global signal_running
    signal_running = False
    await update.message.reply_text("🛑 Auto Signal Stopped")

async def win(update: Update, context: ContextTypes.DEFAULT_TYPE, profit="+৳100"):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"✅ WIN — Profit {profit}\nNext Ready..."
    )

async def auto_signal(context: ContextTypes.DEFAULT_TYPE):
    global signal_running, current_chat_id, preyod_number
    while signal_running and current_chat_id:
        await send_signal(current_chat_id, context)
        preyod_number += 1  # next market period
        await asyncio.sleep(60)  # Wingo 1 Min

async def send_signal(chat_id, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(0, 9)
    bet = "SMALL" if number % 2 == 1 else "BIG"

    message = (
        f"📊 SHAHED AI PREDICTION BOT\n\n"
        f"Preyod number - {preyod_number}\n"
        f"BET - {bet}\n"
        f"Number - {number}\n"
        f"Maintain - 8 level\n\n"
        f"🔹 Join - {REF_LINK}"
    )
    await context.bot.send_message(chat_id=chat_id, text=message)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal_on", signal_on))
    app.add_handler(CommandHandler("signal_off", signal_off))
    app.add_handler(CommandHandler("win", win))

    print("✅ SHAHED AI Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

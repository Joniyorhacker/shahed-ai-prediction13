import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# -------------------------------
# Fixed Config (Secrets here)
# -------------------------------
TOKEN = "8380050511:AAHCU4h9lNDkQJMzU44kxE3Nx-Ujm6JTq2c"
OWNER_ID = 6091430516
REF_LINK = "https://dkwin9.com/#/register?invitationCode=16532572738"

# -------------------------------
# Logger Setup
# -------------------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# -------------------------------
# Global Variables
# -------------------------------
signal_running = False
current_chat_id = None

# -------------------------------
# Commands
# -------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🤖 Welcome to SHAHED AI PREDICTION BOT\n\n"
        f"🔹 This bot gives Wingo 1-min live signals.\n"
        f"🔹 Owner: @shahedbintarek\n"
        f"🔹 Join via link: {REF_LINK}\n\n"
        f"Commands:\n"
        f"/signal_on - Start auto signals\n"
        f"/signal_off - Stop auto signals\n"
        f"/win - Mark last signal as WIN\n"
        f"/loss - Mark last signal as LOSS"
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

async def win(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ WIN — Next Ready")

async def loss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # নতুন সিগন্যাল দিবে, কিছু এক্সট্রা লিখবে না
    await send_signal(update.effective_chat.id, context)

# -------------------------------
# Signal System
# -------------------------------
async def auto_signal(context: ContextTypes.DEFAULT_TYPE):
    global signal_running, current_chat_id
    while signal_running and current_chat_id:
        await send_signal(current_chat_id, context)
        await asyncio.sleep(60)  # প্রতি ১ মিনিট পর নতুন সিগন্যাল

async def send_signal(chat_id, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "📊 SHAHED AI PREDICTION\n\n"
            "BET: SMALL (1,3,5,7,9)\n"
            "STEP MAINTAIN: 8\n\n"
            "✅ Go Safe!"
        )
    )

# -------------------------------
# Main Runner
# -------------------------------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal_on", signal_on))
    app.add_handler(CommandHandler("signal_off", signal_off))
    app.add_handler(CommandHandler("win", win))
    app.add_handler(CommandHandler("loss", loss))

    print("✅ SHAHED AI Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

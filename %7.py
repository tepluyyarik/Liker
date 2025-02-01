import random
import string
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters




def generate_password(length: int = 12) -> str:

    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
def generate_wifi_name()-> str:
    gwords=["Crop","Bingle","Clock","Combine","Single","Flame"]
    fwords=["Nutwin","Grabe", "Fint","Network","iPhone 15Pro"]
    siders = ''.join(random.choices(string.digits, k=5))
    return f"{random.choice(gwords)}_{random.choice(fwords)}_{siders}"


async def password_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password=generate_password()
    await update.message.reply_text(f"Your password generated!{password}")


async def wifi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    wifi_name = generate_wifi_name()
    await update.message.reply_text(f"Your name generated!{wifi_name}")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Привіт! Using command:\n"
        "/password - generate new password\n"
        "/wifi - generate wifi name"
    )
if __name__  == "__main__":
    app = ApplicationBuilder().token("7773751107:AAGww75s7dT6Z6lBl2OLrHFsrzrowzlmwTo").build()





app.add_handler(CommandHandler("password", password_command))
app.add_handler(CommandHandler("wifi", wifi_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
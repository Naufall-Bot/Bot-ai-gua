import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Konfigurasi
TELEGRAM_TOKEN = "7595310672:AAFI8Wdf8cGShPRLMMUI8gU2rx7Jzi6M5hE"  # Ganti dengan token bot Anda
OPENAI_API_KEY = "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"  # Ganti dengan API key OpenAI

# Inisialisasi OpenAI
openai.api_key = OPENAI_API_KEY

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hai! Saya bot AI. Kirim pesan apa saja untuk berinteraksi.")

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    
    # Mengirim permintaan ke OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    
    ai_reply = response.choices[0].message["content"]
    update.message.reply_text(ai_reply)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handler perintah dan pesan
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Mulai bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
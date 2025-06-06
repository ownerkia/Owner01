import os from flask import Flask, request from telegram import Bot, Update from telegram.ext import Dispatcher, CommandHandler

TOKEN = os.environ['BOT_TOKEN'] WEBHOOK_URL = os.environ['WEBHOOK_URL']

app = Flask(name) bot = Bot(TOKEN) dispatcher = Dispatcher(bot, update_queue=None, workers=0)

def start(update, context): update.message.reply_text("سلام! Web App Ownerassets آماده‌ست ✅")

dispatcher.add_handler(CommandHandler('start', start))

@app.route(f'/{TOKEN}', methods=['POST']) def webhook(): update = Update.de_json(request.get_json(force=True), bot) dispatcher.process_update(update) return '', 200

@app.route('/') def index(): return 'Web App Ownerassets در حال اجراست!'

if name == 'main': bot.delete_webhook() bot.set_webhook(WEBHOOK_URL + '/' + TOKEN) app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))


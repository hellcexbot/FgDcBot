import random, asyncio
from time import sleep

from tg_bot.modules.helper_funcs.doguluksoru import DOGRU_SR_TEXT
from tg_bot.modules.helage_id)
        bot.send_message(chat_id=update.effective_chat.id,
                         text=f"🛑 **[{user.first_name}](tg://user?id={user.id}) İçin Cesaret Sorusu Getiriliyor...**",
                         parse_mode=ParseMode.MARKDOWN)
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(CESARET_SR_TEXT)}")

dc_handler = CommandHandler("dc", dc)
dc_dc_handler = CallbackQueryHandler(button)
dispatcher.add_handler(dc_handler)
dispatcher.add_handler(dc_dc_handler)

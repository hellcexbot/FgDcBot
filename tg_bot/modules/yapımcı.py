import importlib
import re
from typing import Optional, List

from tg_bot import dispatcher
from telegram import Message, Chat, Update, Bot, User
from 
@run_async
def sahip(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    msg = update.effective_message  # type: Optional[Message]
    user = update.effective_user

    KEYBOARDS = [[InlineKeyboardButton(text="Sahibim",
                                        url="t.mr/intiqam")]]
    
    KEYBOARDS += [[InlineKeyboardButton(text="Duyuru Kanalım",
                                         url="t.me/AzeBots")]]

    KEYBOARDS += [[InlineKeyboardB
    bot.send_message(chat_id=KOMUT_CHAT_İD,
                         text=KOMUT_CHAT_İD_TEXT.format(user.first_name, user.id, user.id, chat.title, chat.id, "sahip"),
                         parse_mode=ParseMode.MARKDOWN)

sahip_handler = CommandHandl

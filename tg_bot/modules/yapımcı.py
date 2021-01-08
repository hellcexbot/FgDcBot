import importlib
import re
from typing import Optional, List

from tg_bot import dispatcher
from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

@run_async
def sahip(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    msg = update.effective_message  # type: Optional[Message]

    KEYBOARDS = [[InlineKeyboardButton(text="Sahibim",
                                        url="t.me/fireganqq")]]
    
    KEYBOARDS += [[InlineKeyboardButton(text="Duyuru Kanalım",
                                         url="t.me/fireqanqbotlari")]]

    KEYBOARDS += [[InlineKeyboardButton(text="Sahibimin Blog Kanalı",
                                        url="t.me/fireganqblog")]]
    # ONLY send settings in PM
    if chat.type != chat.PRIVATE:
        text = "Sahibim, Sahibimin Kanalları Ve Güncelleme V.b. Duyuru Kanallıma Aşağıdaki Butonlardan Ulaşa Bilirsiniz:)"
        msg.reply_text(text,
                          reply_markup=InlineKeyboardMarkup(KEYBOARDS)
    else:
        text = "Sahibim, Sahibimin Kanalları Ve Güncelleme V.b. Duyuru Kanallıma Aşağıdaki Butonlardan Ulaşa Bilirsiniz:)"
        msg.reply_text(text,
                          reply_markup=InlineKeyboardMarkup(KEYBOARDS)

sahip_handler = CommandHandler("sahip", sahip)
dispatcher.add_handler(sahip_handler)

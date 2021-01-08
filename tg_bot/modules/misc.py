import html
import json
import random
from datetime import datetime
from typing import Optional, List

import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html

from tg_bot import dispatcher
from tg_bot.__main__ import STATS

@run_async
def stats(bot: Bot, update: Update):
    update.effective_message.reply_text("Mevcut istatistikler:\n\n" + "\n".join([mod.__stats__() for mod in STATS]))


STATS_HANDLER = CommandHandler("stats", stats, filters=Filters.user(1340915968))

dispatcher.add_handler(STATS_HANDLER)

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

from tg_bot import dispatcher, OWNER_ID
from tg_bot.__main__ import STATS, USER_INFO
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.extraction import extract_user
from tg_bot.modules.helper_funcs.filters import CustomFilters

RUN_STRINGS = (
    "Nereye gittiğini düşünüyorsun?",
    "Hıı? ne? kaçtılar mı?",
    "ZZzzZZzz... Ha? ne? oh, yine onlar, boşver.",
    "Buraya geri gel!",
    "Çok hızlı değil...",
    "Duvara dikkat edin!",
    "Beni onlarla yalnız bırakma !!",
    "Koşarsan ölürsün.",
    "Sana şakalar, her yerdeyim",
    "Pişman olacaksın...",
    "Ayrıca deneyebilirsin /kickme, bunun eğlenceli olduğunu duydum.",
    "Git başka birini rahatsız et, burada kimse umursamıyor.",
    "Koşabilirsin ama saklanamazsın.",
    "Tüm sahip olduğun bu mu?",
    "Arkandayım...",
    "Misafirin var!",
    "Bunu kolay yoldan veya zor yoldan yapabiliriz.",
    "You just don't get it, do you?",
    "Evet, koşsan iyi olur!",
    "Lütfen bana ne kadar önemsediğimi hatırlatır mısın?",
    "Senin yerinde olsam daha hızlı koşardım.",
    "Bu kesinlikle aradığımız droid.",
    "Olasılıklar senin lehine olsun.",
    "Ünlü son sözler.",
    "Ve sonsuza kadar kayboldular, bir daha asla görülmeyecek.",
    "\"Oh, bana bak! Ben çok iyiyim, bir bottan kaçabilirim!\" - bu kişi",
    "Evet evet, sadece buna dokunun /kickme .",
    "İşte, bu yüzüğü al ve üzerindeyken Mordor'a git.",
    "Efsaneye göre, hala çalışıyorlar...",
    "Harry Potter'ın aksine, ailen seni benden koruyamaz.",
    "Korku, öfkeye yol açar. Öfke nefrete yol açar. Nefret acıya yol açar. Korku içinde koşmaya devam edersen, yapabilirsin "
    "sonraki Vader ol.",
    "Birden fazla hesaplama yaptıktan sonra, saçmalıklarınıza olan ilgimin tam olarak 0 olduğuna karar verdim.",
    "Efsaneye göre, hala çalışıyorlar.",
    "Devam et, yine de seni burada istediğimizden emin değilim.",
    "Sen bir wizasın- Oh. Bekle. Sen Harry değilsin, devam et .",
    "SALONLARDA KOŞMAK YOK!",
    "Güle güle bebek.",
    "Köpekleri kim dışarı bıraktı?",
    "Komik çünkü kimsenin umurunda değil.",
    "Ah, ne yazık. Bunu beğendim.",
    "Açıkçası canım, umurumda değil.",
    "Milkshake'im bütün erkekleri bahçeye getiriyor... O yüzden daha hızlı koş!",
    "Gerçeği idare edemezsin!",
    "Uzun zaman önce, çok uzaktaki bir galakside ... Birisi bunu umursardı. Artık değil.",
    "Hey, şunlara bak! Kaçınılmaz banhammerden kaçıyorlar ... Sevimli.",
    "Önce Han vurdu. Ben de öyle.",
    "Neyin peşinden koşuyorsun, beyaz bir tavşan?",
    "Doktor'un dediği gibi... KOŞ!",
)

SLAP_TEMPLATES = (
    "{item} ile {user1} {hits} {user2}.",
    "{item} ile yüzüne {user1} {hits} {user2}.",
    "{user1} bir {item} ile biraz {user2} {hits}.",
    "{user1}, {user2} konumunda bir {item} {atar}.",
    "{user1} bir {item} alır ve onu {user2} 'nin yüzüne {atar}.",
    "{user1}, {user2} 'nin genel yönünde bir {item} başlatır.",
    "{user1}, aptalca bir {item} ile {user2} tokatlamaya başlar.",
    "{user1}, {user2} sabitler ve tekrar tekrar bir {item} ile {hits}.",
    "{user1} onunla bir {item} ve {hits} {user2} kaptı.",
    "{user1} bir sandalyeye {user2} 'yi bağlar ve onlara bir {item} {atar}.",
    "{user1}, {user2} 'nin lavda yüzmeyi öğrenmesine yardımcı olmak için arkadaşça bir destek verdi."
)

ITEMS = (
    "Demir Döküm tencere",
    "büyük alabalık",
    "beysbol sopası",
    "kriket sopası",
    "tahta kamış-",
    "tırnak",
    "yazıcı",
    "kürek",
    "CRT monitor",
    "fizik ders kitabı",
    "tost makinası",
    "Richard Stallman'ın portresi",
    "televizyon",
    "beş tonluk kamyon",
    "koli bandı rulosu",
    "kitap",
    "laptop",
    "eski televizyon",
    "kaya çuvalı",
    "gökkuşağı alabalığı",
    "plastik tavuk",
    "çivili yarasa",
    "çivili bafire söndürücü",
    "ağır taş",
    "pislik yığını",
    "arı kovanı",
    "çürük et parçası",
    "ayı",
    "tuğla",
)

THROW = (
    "atar",
    "uçuş",
    "chucks",
    "savurmak",
)

HIT = (
    "vuruşlar",
    "vurmak",
    "tokat",
    "şapır şupur",
    "bashes",
)

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"
GMAPS_TIME = "https://maps.googleapis.com/maps/api/timezone/json"


@run_async
def runs(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(RUN_STRINGS))


@run_async
def slap(bot: Bot, update: Update, args: List[str]):
    msg = update.effective_message  # type: Optional[Message]

    # reply to correct message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(msg.from_user.first_name, msg.from_user.id)

    user_id = extract_user(update.effective_message, args)
    if user_id:
        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        if slapped_user.username:
            user2 = "@" + escape_markdown(slapped_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(slapped_user.first_name,
                                                   slapped_user.id)

    # if no target found, bot targets the sender
    else:
        user1 = "[{}](tg://user?id={})".format(bot.first_name, bot.id)
        user2 = curr_user

    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)

    repl = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)


@run_async
def get_bot_ip(bot: Bot, update: Update):
    """ Sends the bot's IP address, so as to be able to ssh in if necessary.
        OWNER ONLY.
    """
    res = requests.get("http://ipinfo.io/ip")
    update.message.reply_text(res.text)


@run_async
def get_id(bot: Bot, update: Update, args: List[str]):
    user_id = extract_user(update.effective_message, args)
    if user_id:
        if update.effective_message.reply_to_message and update.effective_message.reply_to_message.forward_from:
            user1 = update.effective_message.reply_to_message.from_user
            user2 = update.effective_message.reply_to_message.forward_from
            update.effective_message.reply_text(
                "Orijinal gönderen `{}`, `{}` kimliğine sahip.\nİletici, `{}`, `{}` kimliğine sahip.".format(
                    escape_markdown(user2.first_name),
                    user2.id,
                    escape_markdown(user1.first_name),
                    user1.id),
                parse_mode=ParseMode.MARKDOWN)
        else:
            user = bot.get_chat(user_id)
            update.effective_message.reply_text("`{}` kimliği `{}`.".format(escape_markdown(user.first_name), user.id),
                                                parse_mode=ParseMode.MARKDOWN)
    else:
        chat = update.effective_chat  # type: Optional[Chat]
        if chat.type == "private":
            update.effective_message.reply_text("Kimliğiniz: `{}`.".format(chat.id),
                                                parse_mode=ParseMode.MARKDOWN)

        else:
            update.effective_message.reply_text("Bu grubun kimliği `{}`.".format(chat.id),
                                                parse_mode=ParseMode.MARKDOWN)


@run_async
def info(bot: Bot, update: Update, args: List[str]):
    msg = update.effective_message  # type: Optional[Message]
    user_id = extract_user(update.effective_message, args)

    if user_id:
        user = bot.get_chat(user_id)

    elif not msg.reply_to_message and not args:
        user = msg.from_user

    elif not msg.reply_to_message and (not args or (
            len(args) >= 1 and not args[0].startswith("@") and not args[0].isdigit() and not msg.parse_entities(
        [MessageEntity.TEXT_MENTION]))):
        msg.reply_text("Bundan bir kullanıcı çıkaramıyorum.")
        return

    else:
        return

    text = "<b>User info</b>:" \
           "\nID: <code>{}</code>" \
           "\nİsim: {}".format(user.id, html.escape(user.first_name))

    if user.last_name:
        text += "\nSoyadı: {}".format(html.escape(user.last_name))

    if user.username:
        text += "\nKullanıcı adı: @{}".format(html.escape(user.username))

    text += "\nKalıcı kullanıcı bağlantısı: {}".format(mention_html(user.id, "link"))

    if user.id == OWNER_ID:
        text += "\n\nBu kişi benim sahibim - onlara karşı asla bir şey yapmam!"

    for mod in USER_INFO:
        mod_info = mod.__user_info__(user.id).strip()
        if mod_info:
            text += "\n\n" + mod_info

    update.effective_message.reply_text(text, parse_mode=ParseMode.HTML)


@run_async
def get_time(bot: Bot, update: Update, args: List[str]):
    location = " ".join(args)
    if location.lower() == bot.first_name.lower():
        update.effective_message.reply_text("Benim için her zaman banhammer zamanı!")
        bot.send_sticker(update.effective_chat.id)
        return

    res = requests.get(GMAPS_LOC, params=dict(address=location))

    if res.status_code == 200:
        loc = json.loads(res.text)
        if loc.get('status') == 'OK':
            lat = loc['results'][0]['geometry']['location']['lat']
            long = loc['results'][0]['geometry']['location']['lng']

            country = None
            city = None

            address_parts = loc['results'][0]['address_components']
            for part in address_parts:
                if 'country' in part['types']:
                    country = part.get('long_name')
                if 'administrative_area_level_1' in part['types'] and not city:
                    city = part.get('long_name')
                if 'locality' in part['types']:
                    city = part.get('long_name')

            if city and country:
                location = "{}, {}".format(city, country)
            elif country:
                location = country

            timenow = int(datetime.utcnow().timestamp())
            res = requests.get(GMAPS_TIME, params=dict(location="{},{}".format(lat, long), timestamp=timenow))
            if res.status_code == 200:
                offset = json.loads(res.text)['dstOffset']
                timestamp = json.loads(res.text)['rawOffset']
                time_there = datetime.fromtimestamp(timenow + timestamp + offset).strftime("%H:%M:%S on %A %d %B")
                update.message.reply_text("It's {} in {}".format(time_there, location))


@run_async
def echo(bot: Bot, update: Update):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(args[1])
    else:
        message.reply_text(args[1], quote=False)
    message.delete()


@run_async
def gdpr(bot: Bot, update: Update):
    update.effective_message.reply_text("Tanımlanabilir veriler siliniyor...")
    for mod in GDPR:
        mod.__gdpr__(update.effective_user.id)

    update.effective_message.reply_text("Kişisel verileriniz silindi.\n\nBunun engeli kaldırmayacağını unutmayın "
                                        "Marie verisi değil, telgraf verisi olduğu için herhangi bir sohbetten sizi. "
                                        "Sel, uyarılar ve gbans da şu tarihten itibaren korunur: "
                                        "[bu](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
                                        " açıkça silme hakkının geçerli olmadığını belirten"
                                        "\"kamu yararına yürütülen bir görevin yerine getirilmesi için\", olduğu gibi "
                                        "yukarıda belirtilen veri parçaları için durum.",
                                        parse_mode=ParseMode.MARKDOWN)


MARKDOWN_HELP = """
Markdown, telegram tarafından desteklenen çok güçlü bir biçimlendirme aracıdır. emin olmak için {} bazı geliştirmelere sahiptir \
kaydedilen mesajlar doğru şekilde ayrıştırılır ve düğmeler oluşturmanıza olanak sağlar.

- <code>_italic_</code>: `metni '_' ile kaydırmak italik metin üretecektir`
- <code>*bold*</code>: `metni '*' ile kaydırmak kalın metin üretecektir`
- <code>`code`</code>: `metni '`ile kaydırmak,' kod 'olarak da bilinen tek aralıklı metin üretir`
- <code>[sometext](someURL)</code>: `bu bir bağlantı oluşturacaktır - mesaj sadece <code>sometext</code> gösterecektir`, \
ve buna dokunduğunuzda sayfa <code>someURL</code> adresinde açılacaktır.

*ÖRNEĞİN:*
<code>[test](example.com)</code>

- <code>[buttontext](buttonurl:someURL)</code>: bu, kullanıcıların buton oluşturmasını sağlar \
işaretlemelerinde düğmeler. <code>düğme_metni</code>, düğmede görüntülenecek olan ve <code>bir_url</code> olacaktır \
açılan url olacaktır.

*ÖRNEĞİN*:
 <code>[This is a button](buttonurl:example.com)</code>

Aynı satırda birden çok düğme istiyorsanız, şu şekilde kullanın: aynı:
<code>[buton1](buttonurl://example.com)
[buton2](buttonurl://google.com:same)</code>
Bu, her satırda bir düğme yerine tek bir satırda iki düğme oluşturacaktır.

Mesajınızın bir düğmeden başka bir metin içermesi <b>ZORUNLUDUR</b>!
""".format(dispatcher.bot.first_name)


@run_async
def markdown_help(bot: Bot, update: Update):
    update.effective_message.reply_text(MARKDOWN_HELP, parse_mode=ParseMode.HTML)
    update.effective_message.reply_text("Aşağıdaki mesajı bana iletmeyi deneyin, göreceksiniz!")
    update.effective_message.reply_text("/save test Bu bir indirgeme testidir. _italics_, * kalın *, `kod`, "
                                        "[URL](example.com) [button](buttonurl:github.com) "
                                        "[button2](buttonurl://google.com:same)")


@run_async
def stats(bot: Bot, update: Update):
    update.effective_message.reply_text("Mevcut istatistikler:\n" + "\n".join([mod.__stats__() for mod in STATS]))

@run_async
def stickerid(bot: Bot, update: Update):
    msg = update.effective_message
    if msg.reply_to_message and msg.reply_to_message.sticker:
        update.effective_message.reply_text("Merhaba " +
                                            "[{}](tg://user?id={})".format(msg.from_user.first_name, msg.from_user.id)
                                            + ", Yanıtladığınız çıkartma kimliği: :\n```" + 
                                            escape_markdown(msg.reply_to_message.sticker.file_id) + "```",
                                            parse_mode=ParseMode.MARKDOWN)
    else:
        update.effective_message.reply_text("Merhaba " + "[{}](tg://user?id={})".format(msg.from_user.first_name,
                                            msg.from_user.id) + ", Kimlik etiketi almak için lütfen çıkartma mesajını yanıtlayın",
                                            parse_mode=ParseMode.MARKDOWN)
@run_async
def getsticker(bot: Bot, update: Update):
    msg = update.effective_message
    chat_id = update.effective_chat.id
    if msg.reply_to_message and msg.reply_to_message.sticker:
        bot.sendChatAction(chat_id, "typing")
        update.effective_message.reply_text("Merhaba " + "[{}](tg://user?id={})".format(msg.from_user.first_name,
                                            msg.from_user.id) + ", Lütfen aşağıda talep ettiğiniz dosyayı kontrol edin."
                                            "\nLütfen bu özelliği akıllıca kullanın!",
                                            parse_mode=ParseMode.MARKDOWN)
        bot.sendChatAction(chat_id, "upload_document")
        file_id = msg.reply_to_message.sticker.file_id
        newFile = bot.get_file(file_id)
        newFile.download('sticker.png')
        bot.sendDocument(chat_id, document=open('sticker.png', 'rb'))
        bot.sendChatAction(chat_id, "upload_photo")
        bot.send_photo(chat_id, photo=open('sticker.png', 'rb'))
        
    else:
        bot.sendChatAction(chat_id, "typing")
        update.effective_message.reply_text("Merhaba " + "[{}](tg://user?id={})".format(msg.from_user.first_name,
                                            msg.from_user.id) + ", Çıkartma resmi almak için lütfen çıkartma mesajını yanıtlayın",
                                            parse_mode=ParseMode.MARKDOWN)

# /ip is for private use
__help__ = """
 - /id: `mevcut grup kimliğini alın. Bir mesaj yanıtlanarak kullanılırsa, o kullanıcının kimliğini alır.`
 - /runs: `bir yanıt dizisinden rastgele bir dizeyi yanıtlar.`
 - /slap: `bir kullanıcıya tokat atmak ya da bir cevap değilse tokatlanmak.`
 - /time <place>: `verilen yerin yerel saatini verir`.
 - /info: `bir kullanıcı hakkında bilgi alın.`
 - /gdpr: `bilgilerinizi botun veritabanından siler. Yalnızca özel sohbetler.`
 - /markdownhelp: `Markdown'un telgrafta nasıl çalıştığına dair hızlı bir özet - sadece özel sohbetlerde çağrılabilir.`
 - /stickerid: bir çıkartmayı yanıtlayın ve çıkartma kimliğini alın.
 - /getsticker: bir çıkartmayı yanıtlayın ve çıkartmayı .png ve resim olarak alın.
"""

__mod_name__ = "Misc"

ID_HANDLER = DisableAbleCommandHandler("id", get_id, pass_args=True)
IP_HANDLER = CommandHandler("ip", get_bot_ip, filters=Filters.chat(OWNER_ID))

TIME_HANDLER = CommandHandler("time", get_time, pass_args=True)

RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, pass_args=True)
INFO_HANDLER = DisableAbleCommandHandler("info", info, pass_args=True)

ECHO_HANDLER = CommandHandler("echo", echo, filters=Filters.user(OWNER_ID))
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help, filters=Filters.private)

STATS_HANDLER = CommandHandler("stats", stats, filters=CustomFilters.sudo_filter)
GDPR_HANDLER = CommandHandler("gdpr", gdpr, filters=Filters.private)

STICKERID_HANDLER = DisableAbleCommandHandler("stickerid", stickerid)
GETSTICKER_HANDLER = DisableAbleCommandHandler("getsticker", getsticker)


dispatcher.add_handler(ID_HANDLER)
dispatcher.add_handler(IP_HANDLER)
dispatcher.add_handler(TIME_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(INFO_HANDLER)
dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)
dispatcher.add_handler(STATS_HANDLER)
dispatcher.add_handler(GDPR_HANDLER)
dispatcher.add_handler(STICKERID_HANDLER)
dispatcher.add_handler(GETSTICKER_HANDLER)

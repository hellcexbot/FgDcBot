from functools import wraps
from typinly_text("Buradaki mesajları silemiyorum! "
                                                "Yönetici olduğumdan ve diğer kullanıcıların mesajlarını silebildiğimden emin olun.")

    return delete_rights


def can_pin(func):
    @wraps(func)
    def pin_rights(bot: Bot, update: Update, *args, **kwargs):
        if update.enal[User]
        if user and not is_user_admin(update.effective_chat, user.id):
            return func(bot, update, *args, **kwargs)

    return is_not_admin

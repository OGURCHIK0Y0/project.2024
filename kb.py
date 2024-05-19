from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="мячик", callback_data="ball"),
    InlineKeyboardButton(text="гениальные новости нск", callback_data="new")],
    [InlineKeyboardButton(text="кино", callback_data="k"),
    InlineKeyboardButton(text="💰 Баланс", callback_data="m")],
    [InlineKeyboardButton(text="💎 реальные деньги", callback_data="r"),
    InlineKeyboardButton(text="🎁 кубик", callback_data="h")],
    [InlineKeyboardButton(text="бовлинг", callback_data="b"),
    InlineKeyboardButton(text="дартс", callback_data="l")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

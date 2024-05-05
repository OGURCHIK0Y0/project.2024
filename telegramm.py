import asyncio
import logging
from aiogram import F
from random import randint
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7044627094:AAFQklyTsJfBgctPyEEuUmV55PM9L3Qud90")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет меня зовут !лучший бот Данила!я умею разговаритвать и занимать твое время.Пиши команды :/мячик , /дароу , /гениальные_новости_нск , /казино ,/дартс , /бовлинг , /кино")
    
# Хэндлер на команду /start
@dp.message(Command("мячик"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.FOOTBALL)

@dp.message(Command("дароу"))
async def cmd_test1(message: types.Message):
    await message.reply("ку")

# async def cmd_dice(message: types.Message):
#     await message.answer_dice(emoji=DiceEmoji.BASKETBALL)
    
    
@dp.message(Command("гениальные_новости_нск"))
async def cmd_dice(message: types.Message):
    await message.answer('t.me/novostinskrf')
    
@dp.message(Command("кино"))
async def cmd_dice(message: types.Message):
    await message.answer('https://www.kinopoisk.ru/?utm_referrer=wylsa.com')
    
@dp.message(Command("деньги"))
async def cmd_dice(message: types.Message):
    await message.answer('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
@dp.message(Command("реальные_деньги"))
async def cmd_dice(message: types.Message):
    await message.answer('https://www.youtube.com/watch?v=XqZsoesa55w')
    
@dp.message(Command("Твич"))
async def cmd_dice(message: types.Message):
    await message.answer('https://www.twitch.tv/')
    
@dp.message(Command("казино"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.SLOT_MACHINE)
    
@dp.message(Command("дартс"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DART)
    
@dp.message(Command("бовлинг"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)

# Хэндлер на команду /test2
@dp.message(Command("занят?"))
async def cmd_test2(message: types.Message):
    await message.reply("нит,а ты?")

# Где-то в другом месте, например, в функции main():

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
@dp.message(Command("кубик"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

@dp.message(Command("random10"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="жми если хочешь много денег",
        callback_data="random_value")
    )
    await message.answer(
        "я напишу рандомное число от 1 до 10",
        reply_markup=builder.as_markup()
    )
    
@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))

@dp.message(Command("игровые_новости"))
async def cmd_test1(message: types.Message):
    await message.answer('t.me/GamerNewer')
    
@dp.message(Command("реганье"))
async def cmd_реганье(message: types.Message):
    kb = [
        [types.KeyboardButton(text="гитхаб")],
        [types.KeyboardButton(text="почта")],
        [types.KeyboardButton(text="ютуб")],
        [types.KeyboardButton(text="овервульф")],
        [types.KeyboardButton(text="вк")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("куда хотите зарегистрироватся?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "гитхаб")
async def with_puree(message: types.Message):
    await message.reply("https://github.com/")
    
@dp.message(F.text.lower() == "почта")
async def with_puree(message: types.Message):
    await message.reply("https://www.google.com/intl/ru/gmail/about/")
    
@dp.message(F.text.lower() == "ютуб")
async def with_puree(message: types.Message):
    await message.reply("https://www.youtube.com/account_advanced?hl=ru")

@dp.message(F.text.lower() == "овервульф")
async def with_puree(message: types.Message):
    await message.reply("https://stackoverflow.com/")
    
@dp.message(F.text.lower() == "вк")
async def with_puree(message: types.Message):
    await message.reply("https://vk.com/")

if __name__ == "__main__":
    asyncio.run(main())

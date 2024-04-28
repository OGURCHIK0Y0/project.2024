import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji

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
if __name__ == "__main__":
    asyncio.run(main())

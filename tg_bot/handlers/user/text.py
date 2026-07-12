from aiogram import Router, types
from aiogram.filters.command import Command, CommandStart
from tg_bot.utils import read_json
from tg_bot.keyboards.inline import categories_kb

router = Router()

@router.message(CommandStart())
async def on_command_start(message: types.Message):
    categories = read_json('tg_bot/data/categories.json')
    await message.answer(
        f'Привет, {message.from_user.username}!', reply_markup=categories_kb(categories)
    )

@router.message(Command('help'))
async def on_command_help(message: types.Message):
    await message.answer('HELPING!!!')
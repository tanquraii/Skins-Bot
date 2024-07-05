from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboard as kb
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Welcome to valorant skins shop!!!!', reply_markup=kb.main)


@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    await message.answer('Choose type of weapon', reply_markup=await kb.categories())



@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('You chose a weapon')
    await callback.message.answer('Choose a skin to buy',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))



@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('You chose an item')
    await callback.message.answer(f'Name: {item_data.name}\nPrice: {item_data.price}$')
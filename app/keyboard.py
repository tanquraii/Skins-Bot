from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_categories, get_category_item
main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text='Catalog')]
])

async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()#empty keyboard
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name,callback_data=f'category_{category.id}'))#this button is pressed and the callback data is sent
    keyboard.add(InlineKeyboardButton(text='Home',callback_data='Catalog'))
    return keyboard.adjust(2).as_markup()

async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text = item.name,callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(text='Home',callback_data='Catalog'))
    return keyboard.adjust(2).as_markup()
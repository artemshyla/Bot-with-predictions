from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Акции'), 
         KeyboardButton(text='Фьючерсы'), 
         KeyboardButton(text='Облигации')]
         ], 
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню')

stock_list = ['SBER', 'GAZP', 'VTBR', 'SFIN', 'SVCB', 'T', 'LKOH']

async def inline_stocks():
    keyboard = InlineKeyboardBuilder()
    for stock in sorted(stock_list):
        keyboard.add(InlineKeyboardButton(text=stock, callback_data=f'stock_{stock}'))
    return keyboard.adjust(2).as_markup()


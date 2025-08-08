from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, CommandObject

import app.keyboards as kb



router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот, который прогнозирует акции на Московской бриже (MOEX)")
    await message.answer("Выберите вид ценных бумаг", reply_markup=kb.main)

@router.message(F.text == 'Акции')
async def stocks(message: Message):
    await message.answer('Выберите желаемый тикер', reply_markup=await kb.inline_stocks())

@router.callback_query(F.data.startswith('stock_'))
async def selected_stock(callback: CallbackQuery):
    ticker = callback.data.removeprefix('stock_')
    await callback.message.answer(f'Вы выбрали акции {ticker}')
    await callback.answer()
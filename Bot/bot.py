import requests
import json
import asyncio
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
URL = "http://127.0.0.1:8000/api/"
bot = Bot(token="2121024160:AAEdOTKuDg5HNie1Vi7FwoGOk7_jAXpV3EM")
dp = Dispatcher(bot, storage=MemoryStorage())


class Track(StatesGroup):
    question = State()


@dp.message_handler(commands="start")
async def cmd_start(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Узнать информацию о заказе", "Подписаться на обновления"]
    keyboard.add(*buttons)
    await msg.answer("Что вы хотите сделать?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Узнать информацию о заказе"), state=None)
async def Nomer_Zakaza(msg: types.Message):
    await Track.question.set()
    await msg.reply("Напишите номер Заказа", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Track.question)
async def Otslezivanie(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tracknomer'] = msg.text
        data = requests.get(URL + "orders/" + data['tracknomer']).text
        d = json.loads(data)
        await bot.send_message(msg.from_user.id, d['status']['name'])
    await state.finish()


@dp.message_handler(Text(equals="Подписаться на обновления"))
async def Podpiska(msg: types.Message):

    data1 = requests.get(URL + "stock/").text
    headers = {"Content-Type": "application/json", }
    payload = {"user_id": str(msg.from_user.id)}
    requests.post(URL + "bot/", data=json.dumps(payload), headers=headers)


async def rassilka(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        data = requests.get(URL + "stock/").text
        d = json.loads(data)
        headers = {"Content-Type": "application/json", }
        for i in d:
            payload = {"pk": i['pk'], 'published': True}
            data2 = requests.get(URL + "bot/").text
            datajson2 = json.loads(data2)
            for j in datajson2:
                await bot.send_message(j['user_id'], i['text'], reply_markup=types.ReplyKeyboardRemove())
                requests.put(URL + "edit-stock/", data=json.dumps(payload), headers=headers)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(rassilka(60))
    main()

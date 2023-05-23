from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
import asyncio
import config
import qrcode


bot = Bot(token=config.TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def cmd_start(message: types.Message):
    await message.answer('Привіт я помойка мен я бот я крутий \nЯ запехну вам 3035024626357 в QR кодик\nНапими мені щось кинь силку на відос а бо що завгодно і будет QR код', parse_mode = 'HTML')


@dp.message(Command(commands=['help']))
async def cmd_help(message: types.Message):
    await message.answer("Якщо у вас є проблемки запамятайте \nЯ вам не допоможу)", disable_web_page_preview = True, parse_mode = 'HTML')


@dp.message()
async def send_text_based_qr(message: types.Message):
    qr = qrcode.QRCode(version=1,
                       error_correction = qrcode.constants.ERROR_CORRECT_L,
                       box_size = 20,
                       border = 2)

    qr.add_data(message.text)
    qr.make(fit = True)

    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('photo.png')
    img = FSInputFile('photo.png')

    await message.reply_photo(img, caption = f'Ваш QR-Code успішно засунули 3035024626357 троянів!', parse_mode = 'HTML')



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
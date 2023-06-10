import os
import soundfile as sf
from pydub import AudioSegment
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

TOKEN = ''

# Загрузка предварительно обученной модели и процессора
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функция конвертации аудиофайла из .ogg в .wav
def convert_ogg_to_wav(ogg_file_path, wav_file_path):
    sound = AudioSegment.from_ogg(ogg_file_path)
    sound.export(wav_file_path, format="wav")

# Обработка команды /start
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который может распознавать русскую речь из голосовых сообщений. Попробуйте отправить мне голосовое сообщение!")

# Обработка голосовых сообщений
@dp.message_handler(content_types=['voice'])
async def analyze(message: types.Message):
    file_id = message.voice.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    await bot.download_file(file_path, 'voice.ogg')

    # Конвертация из .ogg в .wav
    convert_ogg_to_wav('voice.ogg', 'voice.wav')

    # Распознавание речи
    audio_input, _ = sf.read('voice.wav')
    input_values = processor(audio_input, return_tensors='pt', sampling_rate=16_000).input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    # Отправка расшифрованного текста обратно пользователю
    await message.reply(transcription)

# Запуск бота
if __name__ == '__main__':
    start_polling(dp)

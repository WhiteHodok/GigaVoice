# GigaVoice

![dream_TradingCard (2)](https://github.com/WhiteHodok/GigaVoice/assets/39564937/9a2726c6-a315-48c5-a004-e16f71c8c63d)

Этот бот создавался с целью расшифровки голосовых сообщений от пользователей(так как телеграм оборзел и просит деньги за расшифроку гс) , ниже можно увидеть то , c чем можно столкнуться , если не дообучить модель (kaggle в помощь):


![image](https://github.com/WhiteHodok/GigaVoice/assets/39564937/543a6a22-30b9-4827-aa1c-f5002a4e16f4)

Сам бот(я его не хощу, он жрёт много): https://t.me/GigaVoice_bot

Что будет в консоли если запустить "сырую модель":

```sh
Some weights of Wav2Vec2ForCTC were not initialized from the model checkpoint at facebook/wav2vec2-large-960h and are newly initialized: ['wav2vec2.masked_spec_embed']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
```

## Зависимости (не наркотические)

- soundfile
- pydub
- aiogram
- transformers
- torch

**Установка зависимостей:**

```sh
pip install -r requirements.txt
```

## Как выглядит конвертер from .ogg to .wav

```sh
def convert_ogg_to_wav(ogg_file_path, wav_file_path):
    sound = AudioSegment.from_ogg(ogg_file_path)
    sound.export(wav_file_path, format="wav")
```

## Что нужно налепить в dev ветки для хорошей жизни

- Обработку исключений для бота


## Проект на будущее

- SD бот с теми же плюшками, но для генерации изображений (ага щас где время на него взять)
- Создать LORA обученную на фотках Илюши



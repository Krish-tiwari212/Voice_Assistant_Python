import sounddevice as sd
import wavio as wv
import openai
from gtts import gTTS
import os

openai.api_key = "your api key"

freq = 44100
duration = 4
print("Ask Me Something")
recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
sd.wait()
wv.write("recording1.mp3", recording, freq, sampwidth=2)
audio_file = open("recording1.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript['text'])
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant that provides the correct answer in a funny way."},
        {"role": "user", "content": transcript['text']},
    ]
)
print(response['choices'][0]['message']['content'])
mytext = response['choices'][0]['message']['content']
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False, tld="co.in")

myobj.save("welcome.mp3")

os.system("start welcome.mp3")
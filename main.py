from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json
import pyttsx3
import core
from core import SystemInfo as SystemInfo

#Sintetizador de voz

engine = pyttsx3.init()
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[2].id)



def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
# Reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala
print('Já Pode Falar')
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        
        if result is not None:
            text = result['text']
            
            print(text)
            
            if text == 'que horas são' or text == 'me diga as horas':
                speak(SystemInfo.get_time())
                
            elif text == 'que dia é hoje':
                speak(SystemInfo.get_day())
                
            else:
                speak('Não entendi, pode repetir?')
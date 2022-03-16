import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[2].id)
engine.say("Olá Jéssica, meu nome é Ana, sou a nova assistente pessoal do seu marido!")
engine.runAndWait()

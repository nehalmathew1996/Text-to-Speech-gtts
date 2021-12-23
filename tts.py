import os
from gtts import gTTS

#input_text='Hi! My name is Nehal. How may I help you?'

file=open('input.txt','r') #.replace("\n"," ")
input_text=file.read()

language='en' # or 'fr' for french

output =gTTS(text=input_text,lang=language, slow= False)

output.save("output.mp3")

file.close()

os.system("start output.mp3")


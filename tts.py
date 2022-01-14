import os
from gtts import gTTS

#input_text='Hi! My name is Nehal. How may I help you?'

file=open('input.txt','r') #.replace("\n"," ")
input_text=file.read()

language='en' # or 'fr' for french

output =gTTS(text=input_text,lang=language, slow= False)

output.save("output.mp3")

file.close()


# Converting mp3 to wav file 

# # To play audio
# os.system("output.mp3")
from os import path
from pydub import AudioSegment

# files                                                                         
src = "output.mp3"
dst = "output.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst  , format="wav")

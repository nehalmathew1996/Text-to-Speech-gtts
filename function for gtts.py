def tts(message,file_name,path):

    language='en' # or 'fr' for french

    output =gTTS(text=message,lang=language, slow= False)

    output.save(path+file_name+'.mp3')

    # Converting mp3 to wav file 

    # # To play audio
    # os.system("output.mp3")

    # files                                                                         
    src = path+file_name+'.mp3'
    dst = path+file_name+'.wav'

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst  , format="wav")

    os.remove(path+file_name+'.mp3')


from gtts import gTTS

import os

def text_tospeech(result):
    mytext = result
    
    language = 'en'
    
    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("translated.mp3")
    
    # os.system("translated.mp3")

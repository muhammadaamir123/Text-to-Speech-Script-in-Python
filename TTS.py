#Import the libraries
from gtts import gTTS
import os

class tts:
    def __init__(self, text):
        self.text = text
        
    
    def convertText(self):
        myText = self.text
        language = 'en'
        
        textSpeech = gTTS(text = myText, lang = language, slow = False)
        textSpeech.save('audio.mp3')
        
        #play converted audio
        #os.system('mpg321 audio.mp3')
        
myText = "Hello, this Text to Speech script written in Python"
obj = tts(myText)
obj.convertText()
import pyttsx3
from resources import GlobalVariable


class SpeechService:
    @staticmethod
    def speak(text):
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 180)

        GlobalVariable.setValue(text)
        print(text)
        
        engine.say(text)
        engine.runAndWait()

       

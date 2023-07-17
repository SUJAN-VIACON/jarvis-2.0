import pyttsx3
from jarvis.GlobalVariable import GlobalVariable

class SpeechService:
    @staticmethod
    def speak(text):
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 180)
        engine.say(text)
        engine.runAndWait()

        GlobalVariable.setValue(text)
        print(text)

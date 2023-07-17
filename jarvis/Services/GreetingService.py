import datetime
from .SpeechService import SpeechService

class GreetingService:
    @staticmethod
    def wishMe():
        hour = datetime.datetime.now().hour

        if hour >= 0 and hour < 12:
            SpeechService.speak("Good Morning mister sujan")
        elif hour >= 12 and hour < 18:
            SpeechService.speak("Good Afternoon mister sujan")
        else:
            SpeechService.speak("Good Evening mister sujan")

        SpeechService.speak("How may I help you, sir?")

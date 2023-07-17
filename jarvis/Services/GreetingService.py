import datetime
from .SpeechService import SpeechService

import os
from dotenv import load_dotenv

load_dotenv()


class GreetingService:
    @staticmethod
    def wishMe():
        owner_name = os.getenv("OWNER_NAME")
        gender = os.getenv("GENDER")
        greeting = os.getenv("GREETING")
        hour = datetime.datetime.now().hour

        if hour >= 0 and hour < 12:
            SpeechService.speak("Good Morning " + owner_name)
        elif hour >= 12 and hour < 18:
            SpeechService.speak("Good Afternoon " + owner_name)
        else:
            SpeechService.speak("Good Evening " + owner_name)

        SpeechService.speak("How may I help you," + greeting + "?")

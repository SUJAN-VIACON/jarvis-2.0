import datetime
import random
import requests
import sys

from .SpeechService import SpeechService

import os
from dotenv import load_dotenv

load_dotenv()


class GreetingService:
    @staticmethod
    def wishMe():
        owner_name = os.getenv("OWNER_NAME")
        hour = datetime.datetime.now().hour

        if hour >= 0 and hour < 12:
            SpeechService.speak("Good Morning " + owner_name)
        elif hour >= 12 and hour < 18:
            SpeechService.speak("Good Afternoon " + owner_name)
        else:
            SpeechService.speak("Good Evening " + owner_name)

        messages = [
            "May your day be filled with sunshine, smiles, and all the little things that make life beautiful.",
            "Wishing you a day as bright as your smile and as magical as your dreams.",
            "Sending you positive vibes for a day that's as fantastic as you are!",
            "May your day be sprinkled with joy, laughter, and the warmth of love.",
            "Here's to a day that surpasses all expectations and leaves you with wonderful memories.",
            "May your day be a canvas of happiness, painted with the colors of laughter and kindness.",
            "Wishing you a day so amazing, it'll be hard to believe it's real!",
            "I hope your day is filled with pleasant surprises, like the first sip of coffee in the morning.",
            "May your day be blessed with serendipitous moments and delightful encounters.",
            "Wishing you a day that's better than a bouquet of your favorite flowers.",
        ]

        random_key = random.randint(0, len(messages) - 1)
        SpeechService.speak(messages[random_key])

        messages = [
            "Is there anything specific you need help with today? I'm here to assist you!",
            "How can I be of service? Feel free to ask any questions or share your concerns.",
            "I'm here to help! Let me know what you need, and I'll do my best to assist you.",
            "If there's anything I can do to make your experience better, just let me know!",
            "Need a hand with something? I'm at your service and ready to help.",
            "Is there a particular topic you'd like to know more about? I'll be glad to provide information and answers.",
            "If there's a problem you're facing, don't hesitate to reach out—I'm here to support you.",
            "How may I be of assistance today? Let me know, and I'll get right on it!",
            "If there's any way I can make your interaction smoother, please don't hesitate to tell me.",
            "I'm here as your virtual assistant. Just tell me how I can assist you, and I'll do my best to fulfill your request.",
        ]

        SpeechService.speak(messages[random_key])

    def connect(host="http://google.com"):
        try:
            response = requests.get(host, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            # If an exception occurred during the request, return False (not connected)
            return False

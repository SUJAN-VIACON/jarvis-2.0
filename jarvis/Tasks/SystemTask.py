from jarvis.Services.SpeechService import SpeechService
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import sys
import keyboard


class SystemTask:
    def answerQuestion(self, question):
        if "how are you" in question:
            SpeechService.speak("i am fine sir")
            SpeechService.speak("whats about you? ")

        if "hello" in question or "hi" in question:
            SpeechService.speak("hii sir")

        if "fine" in question:
            SpeechService.speak("ok sir tell me how can i help you")

        if "good morning" in question:
            SpeechService.speak("good morning sir and wish a very good day to you")

        if "thank you" in question:
            SpeechService.speak("welcome sir")

        # if "shutdown" in question:
        #     os.system("shutdown /s /t 1")

        if "are you there" in question:
            SpeechService.speak("yes sir i am always with you")

        if "who is" in question:
            SpeechService.speak("ok sir i am searching from wikipidia")
            result = question.replace("who is", "")
            print(result)
            result = self.wiki(result)
            print(result)
            SpeechService.speak(result)
            if result == 0:
                SpeechService.speak("i cannot found sir. try by another id")

    def wiki(self, query):
        try:
            return wikipedia.summary(query, sentences=2)
        except Exception as e:
            return "none"

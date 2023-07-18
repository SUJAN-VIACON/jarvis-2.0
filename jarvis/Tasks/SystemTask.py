from resources import SpeechService
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import sys
import keyboard
import subprocess


class SystemTask:
    def answerQuestion(self, question):
        if "who are you" in question:
            SpeechService.speak("i am jarvis you personal virtual assistant.")
            SpeechService.speak("i am created by mister sujan moi.")

        if "how are you" in question:
            SpeechService.speak("i am fine")
            SpeechService.speak("whats about you? ")

        if "yes" in question or "no" in question:
            SpeechService.speak("okk")

        if "hello" in question or "hi" in question:
            SpeechService.speak("hii")

        if "fine" in question:
            SpeechService.speak("ok tell me how can i help you")

        if "good morning" in question:
            SpeechService.speak("good morning and wish a very good day to you")

        if "thank you" in question:
            SpeechService.speak("welcome")

        if "are you there" in question:
            SpeechService.speak("yes i am always with you")

        if "who is" in question:
            SpeechService.speak("ok i am searching from wikipidia")
            result = question.replace("who is", "")
            print(result)
            result = self.wiki(result)
            print(result)
            SpeechService.speak(result)
            if result == 0:
                SpeechService.speak("i cannot found. try by another id")

    def wiki(self, query):
        try:
            return wikipedia.summary(query, sentences=2)
        except Exception as e:
            return "none"

    def shutdown(self, query):
        os.system("shutdown /s /t 1")

    def openInstagram(self, query):
        self.run_cmd_command("start www.instagram.com")
        self.run_cmd_command("exit")

    def openFacebook(self, query):
        self.run_cmd_command("start www.facebook.com")
        self.run_cmd_command("exit")

    def openGoogle(self, query):
        self.run_cmd_command("start www.google.com")
        self.run_cmd_command("exit")

    def openNotepad(self, query):
        apath = "C:\\windows\\system32\\notepad.exe"
        os.startfile(apath)

    def closeLastTab(self, query):
        os.system("taskkill /f /im notepad.exe")
        os.system("taskkill /f /im chrome.exe")

    def lockScreen(self, query):
        self.run_cmd_command("rundll32.exe user32.dll, LockWorkStation")
        self.run_cmd_command("exit")

    def searchOnGoogle(self, query):
        SpeechService.speak("i am searching on google")
        pywhatkit.search(query)

    def playYoutube(self, query):
        song = query.replace("play", "")
        SpeechService.speak("i am searching on youtube")
        pywhatkit.playonyt(song)

    def run_cmd_command(self, command):
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        output, error = process.communicate()

        # Decode the output and error messages
        output = output.decode("utf-8")
        error = error.decode("utf-8")

        # Print the output and error messages
        print("Output:")
        print(output)
        print("Error:")
        print(error)

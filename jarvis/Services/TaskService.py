import random
from .SpeechService import SpeechService
from .SpeechRecognitionService import SpeechRecognitionService
from .SpeechService import SpeechService

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(parent_dir)

from GlobalVariable import GlobalVariable
from Tasks.SystemTask import SystemTask


class TaskService:
    def executableTask(self):
        st = SystemTask()
        return {
            "who are you": st.answerQuestion,
            "yes": st.answerQuestion,
            "no": st.answerQuestion,
            "how are you": st.answerQuestion,
            "hello": st.answerQuestion,
            "fine": st.answerQuestion,
            "good morning": st.answerQuestion,
            "thank you": st.answerQuestion,
            "are you there": st.answerQuestion,
            "who is": st.answerQuestion,
            "shutdown": st.shutdown,
            "open instagram": st.openInstagram,
            "open facebook": st.openFacebook,
            "open notepad": st.openNotepad,
            "open google": st.openGoogle,
            "close it": st.closeLastTab,
            "lock": st.lockScreen,
            "search": st.searchOnGoogle,
            "play": st.playYoutube,
            # "call sujan": st.callSujan,
        }

    def checkAndExecute(self, query):
        self.isExecuted = False

        for keyword, callback in self.executableTask().items():
            if keyword in query:
                callback(query)
                self.isExecuted = True
                break

        if self.isExecuted:
            messages = [
                "Is there anything else I can support you with?",
                "Do you require further assistance from me?",
                "Are there any other ways I can be of help?",
                "Is there something else I can aid you in?",
                "Do you need assistance with anything else?",
                "Is there another matter I can assist you with?",
                "Let me know if there's anything else I can help you with.",
                "Is there any other way I can be of service?",
                "Do you have any other questions I can answer?",
                "Is there anything else you'd like me to assist you with?",
            ]
            random_key = random.randint(0, len(messages) - 1)
            SpeechService.speak(messages[random_key])
            return

        self.apologies()

    def performTask(self):
        while True:
            speech_recognition_service = SpeechRecognitionService()
            query = speech_recognition_service.recognizerVoice()
            GlobalVariable.setValue(query)
            if "go to sleep" in query:
                SpeechService.speak("ok sir i am going to sleep ")
                SpeechService.speak(
                    "i am always with you just say wake up jarvis........."
                )
                break
            self.checkAndExecute(query)

    def apologies(self):
        messages = [
            "I am sorry but I cannot understand what do you mean by that",
            "Sorry, Could You please repeat",
            "I apologies! but are you sure this task is present in my system",
            "Could not get your point could you rephrase it",
        ]

        random_key = random.randint(0, len(messages) - 1)
        SpeechService.speak(messages[random_key])

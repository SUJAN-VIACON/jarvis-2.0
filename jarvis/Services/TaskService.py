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
            "how are you": st.answerQuestion,
            "hello": st.answerQuestion,
            "fine": st.answerQuestion,
            "good morning": st.answerQuestion,
            "thank you": st.answerQuestion,
            "are you there": st.answerQuestion,
            "who is": st.answerQuestion,
        }

    def checkAndExecute(self, query):
        self.isExecuted = False

        for keyword, callback in self.executableTask().items():
            if keyword in query:
                callback(query)
                self.isExecuted = True
                break

        if self.isExecuted:
            return

        self.apologies()

    def performTask(self):
        while True:
            speech_recognition_service = SpeechRecognitionService()
            query = speech_recognition_service.recognizerVoice()
            GlobalVariable.setValue(query)
            self.checkAndExecute(query)

    def apologies(self):
        messages = [
            "I am sorry but I cannot understand what do you mean by that",
            "Sorry, Could You please repeat",
            "I apologies! but are you sure this task is present in my system",
            "Could not get your point could you rephrase it",
        ]

        random_key = random.randint(0, len(messages))
        SpeechService.speak(messages[random_key])

import random
from jarvis.Tasks.SystemTask import SystemTask
from .SpeechService import SpeechService
from .SpeechRecognitionService import SpeechRecognitionService
from .SpeechService import SpeechService

from jarvis.GlobalVariable import GlobalVariable
from jarvis.Tasks import SystemTask


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

    #########  all call back function #############

    def test(self, query):
        SpeechService.speak(query)

        

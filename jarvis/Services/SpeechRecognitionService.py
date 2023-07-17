import speech_recognition as sr
from jarvis.GlobalVariable import GlobalVariable

class SpeechRecognitionService:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.sourceMicrophone = sr.Microphone(device_index=1)

    def recognizerVoice(self):
        with self.sourceMicrophone as source:
            GlobalVariable.setValue("l i s t i n g..................")
            print("l i s t i n g..................")

            audio = self.recognizer.listen(source, phrase_time_limit=3)
        try:
            GlobalVariable.setValue("recognizing................")
            print("recognizing................")

            query = self.recognizer.recognize_google(audio, language="en-in")
            query = query.lower()
            if "jarvis" in query:
                query = query.replace("jarvis", "")

            print(f"user said:{query}\n")

        except Exception as e:
            return "none"
        return query

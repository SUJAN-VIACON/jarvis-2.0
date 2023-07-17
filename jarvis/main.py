import sys
from sys import exit
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.jarvis_ui import Ui_Form

from resources import GlobalVariable
from resources import TaskService
from resources import SpeechService
from resources import GreetingService
from resources import SpeechRecognitionService


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        GreetingService.wishMe()

        while True:
            if __name__ == "__main__":
                speech_recognition_service = SpeechRecognitionService()
                self.permission = speech_recognition_service.recognizerVoice()

                if "wake up" in self.permission:
                    SpeechService.speak("sir tell what would i do for you")
                    basic_task_service = TaskService()
                    basic_task_service.performTask()

                elif "goodbye" in self.permission:
                    SpeechService.speak("ok sir")
                    SpeechService.speak("good bye.........")
                    sys.exit()


class Main(QMainWindow):
    startExecution = MainThread()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.startTask()
        # self.ui.pushButton_2.clicked.connect(self.startTask)
        self.ui.pushButton.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("./src/images/wave.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("./src/images/dribbbble.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("./src/images/neonglobe.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("./src/images/loading_Screen.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("./src/images/ironman.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("./src/images/wave-ball.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        self.ui.textBrowser_3.setText(GlobalVariable.getValue())


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

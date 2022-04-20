from socket import timeout
from socket import *
from sqlite3 import Date
from urllib import request
import pyttsx3
import datetime
import speech_recognition as sr #For recognizing my speech
import pyaudio                  # For using the Microphone
import wikipedia #used the command pip install wikipedia to get this module
import webbrowser as wb #For opening browser
import os
import random
import requests
import pyautogui
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from JarvisGUI import Ui_JarvisFrontEnd
import pywhatkit as kit
import psutil
import pyjokes



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 190 #I am setting the speed of the voice, 140 means 140 words per minute
engine.setProperty('rate', newVoiceRate)


 
def speak(audio): #this function is used for converting text to speech
    engine.say(audio)
    engine.runAndWait()

# speak("Initializing Jarvis")

url = "https://www.google.com/"
timeout = 5

# try: 
#     request = requests.get(url, timeout=timeout)
#     print("Internet connection detected")
#     speak("Connected to Internet")
#     speak("All systems Online")
# except (requests.ConnectionError, requests.Timeout) as exception:
#     print("No internet Detected")
#     print("All systems offline")
#     exit()


def time(): #This Function can say what time it is
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time at the moment is:")
    speak(time)

def date(): #This Function can say what date it is 
    speak("The date today is:")
    today = Date.today()
    date_today = today.strftime("%B %d %Y")
    speak(date_today)

def wishMe(): #This wish will execuse every time I start up this software
    hour = datetime.datetime.now().hour
    print(hour)
    if(hour >= 6 and hour <= 12):
        speak("Good Morning, Boss!")
    elif(hour>12 and hour<=18 ):
        speak("Good Afternoon, Boss!")
    elif(hour>18 and hour<=23):
        speak("Good Evening, Boss!")
    else:
        speak("Good Night Boss!")
    speak("Hello! JARVIS at your service")
    # time()
    # date()
    speak("What can I assist you with?")
    speak("I am Listening")

def screenshot(): 
    img = pyautogui.screenshot()
    img.save("E:\Books\CSE 410\JARVIS AI Assistant\JARVIS_AI_Assistant\JARVIS\Screenshots\ss.png")

def cpu(): 
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)

def jokes():
    speak(pyjokes.get_joke())

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        speak("Initializing Jarvis")
        try: 
            request = requests.get(url, timeout=timeout)
            print("Internet connection detected")
            speak("Connected to Internet")
            speak("All systems Online")
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet Detected")
            print("All systems offline")
            exit()
        
        self.taskExecution()

    def takeCommand(self):  #This is the function which recognizes my speech
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en=US')
            # speak(query)
        except Exception as e:
            print(e)
            speak("Sorry, I can't hear you")
            return "None"
        return query


    # if __name__ =="__main__": #Implementing the main function
    def taskExecution(self):
        clear = lambda: os.system('cls')
        clear()
        wishMe()
        
        while True:
            self.query = self.takeCommand().lower()
            print(self.query)

            if "time" in self.query: #1. For knowing time
                time()
            elif "date" in self.query: #2. For knowing date
                date()
            elif "offline" in self.query: #3. For putting the system offline
                speak("Going Offline")
                quit()
            elif "wikipedia" in self.query: #4. For searching in Wikipedia
                speak("Searching")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary (query, sentences = 2)
                speak(result)
            elif "how are you" in self.query: #5. For normal conv(1)
                speak("I am fine, Thank you!")
                speak("What about you")
            elif "good" in self.query: #6. For normal conv(2)
                speak("I'm glad to hear that.")
                speak("what do you want me to do?")

            elif "fine" in self.query: #7. For normal conv(3)
                speak("I'm glad to hear that.")
                speak("what do you want me to do?")


            elif "open chrome" in self.query: #8. For browsing chrome
                speak("Where should I go?")
                chromepath = "C:/Users/DOLPHIN/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                
                search = self.takeCommand().lower()
                wb.get(chromepath).open_new_tab(search + ".com")
            elif "search in chrome" in self.query: #9. For searching chrome
                chromepath = "C:/Users/DOLPHIN/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                speak("What should I search for?")
                query = self.takeCommand().lower()
                query = query.replace("search for", "")
                speak("Searching for"+query+"in chrome")
                wb.get(chromepath).open("https://www.google.com/search?q="+query)
                

            elif "play a song" and "device" in self.query: #10. Playing a song from Device
                songs_dir = "C:/Users/DOLPHIN/Downloads/Music"
                songs = os.listdir(songs_dir)
                n = random.randint(0, 107)
                os.startfile(os.path.join(songs_dir, songs[n] ))
            
            elif "play a song" and "youtube" in self.query: #11. Playing a song from Youtube
                speak("what song should i play?")
                query = self.takeCommand().lower()
                query = query.replace("play", "")
                kit.playonyt(query)

            elif "screenshot" in self.query: #12. For taking Screenshot
                screenshot()
                speak("screenshot taken")

            elif "cpu" in self.query: #13. For getting the cpu update
                cpu()

            elif "joke" in  self.query:
                jokes()


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisFrontEnd()
        self.ui.setupUi(self)
        self.ui.Run.clicked.connect(self.startTask)
        self.ui.Run_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:\Books\CSE 410\JARVIS AI Assistant\JARVIS_AI_Assistant\Iron Dad and Spider Son One-Shots.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        Label_time = current_time.toString('hh: mm: ss')
        Label_date = current_date.toString(Qt.ISODate) 

        self.ui.textBrowser.setText("Date:"+Label_date)
        self.ui.textBrowser_2.setText("Time:"+Label_time)

app = QApplication(sys.argv)
Jarvis = Main()
Jarvis.show()
exit(app.exec_())





# takeCommand()



# time()
# date()

# speak("Hello World! I am JARVIS and I am here to serve Mehedy.")
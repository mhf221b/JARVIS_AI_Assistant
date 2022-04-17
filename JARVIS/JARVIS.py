from socket import timeout
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
import tkinter as tk
import requests
import pyautogui
import win32api
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 190 #I am setting the speed of the voice, 140 means 140 words per minute
engine.setProperty('rate', newVoiceRate)


 
def speak(audio): #this function is used for converting text to speech
    engine.say(audio)
    engine.runAndWait()

speak("Initializing Jarvis")

url = "https://www.google.com/"
timeout = 5

# try: 
#     request = requests.get(url, timeout=timeout)
#     print("Internet connection detected")
#     speak("Connected to Internet")
#     speak("All systems Online")
# except (requests.ConnectionError, requests.Timeout) as exception:
    # print("No internet Detected")
    # print("All systems offline")
    # exit()

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

def takeCommand():  #This is the function which recognizes my speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en=US')
        speak(query)
    except Exception as e:
        print(e)
        speak("Sorry, I can't hear you")
        return "None"
    return query

# screen_main = tk.Tk()
# screen_main.configure(background='black') #Color of the main background window
# screen_main.attributes('-fullscreen', True) #Window should be full screen


# def color_changer():
#     color = ['red', 'gold', 'silver', 'cyan', 'magenta']
#     actual_color = random.choice(color)
#     label.configure(foreground=actual_color)
#     label.after(500, color_changer)

# label = Label(screen_main, font = ('Arial', 35), text="Welcome to Avengers", background = 'black')
# color_changer()
# label.place(x=1060, y=50)
# screen_main.mainloop()

# if __name__ =="__main__": #Implementing the main function
#     clear = lambda: os.system('cls')
#     clear()
#     wishMe()
    
#     while True:
#         query = takeCommand().lower()
#         print(query)

#         if "time" in query:
#             time()
#         elif "date" in query:
#             date()
#         elif "offline" in query:
#             speak("Going Offline")
#             quit()
#         elif "wikipedia" in query:
#             speak("Searching")
#             query = query.replace("wikipedia", "")
#             result = wikipedia.summary (query, sentences = 2)
#             speak(result)
#         elif "how are you" in query:
#             speak("I am fine, Thank you!")
#             speak("What about you")
#         elif ("good" or "fine") in query:
#             speak("I'm glad to hear that")

#         elif "open chrome" in query:
#             speak("Where should I go?")
#             chromepath = "C:/Users/DOLPHIN/AppData/Local/Google/Chrome/Application/chrome.exe %s"
            
#             search = takeCommand().lower()
#             wb.get(chromepath).open_new_tab(search + ".com")
#         elif "search in chrome" in query:
#             chromepath = "C:/Users/DOLPHIN/AppData/Local/Google/Chrome/Application/chrome.exe %s"
#             speak("What should I search for?")
#             query = takeCommand().lower()
#             query = query.replace("search for", "")
#             speak("Searching for"+query+"in chrome")
#             wb.get(chromepath).open("https://www.google.com/search?q="+query)
            

#         elif "play a song" in query:
#             songs_dir = "C:/Users/DOLPHIN/Downloads/Music %s"
#             songs = os.listdir(songs_dir)
#             n = random(0, 107)
#             os.startfile(os.path.join(songs_dir, songs[n] ))



# takeCommand()



# time()
# date()

# speak("Hello World! I am JARVIS and I am here to serve Mehedy.")


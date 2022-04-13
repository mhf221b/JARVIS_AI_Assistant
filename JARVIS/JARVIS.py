
from sqlite3 import Date
import pyttsx3
import datetime
import speech_recognition as sr #For recognizing my speech
import pyaudio                  # For using the Microphone
import wikipedia #used the command pip install wikipedia to get this module
import webbrowser as wb #For opening browser


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 190 #I am setting the speed of the voice, 140 means 140 words per minute
engine.setProperty('rate', newVoiceRate)

def speak(audio): #this function is used for converting text to speech
    engine.say(audio)
    engine.runAndWait()

def time(): #This Function can say what time it is
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time at the moment is:")
    speak(time)

def date(): #This Function can say what date it is
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The date today is:")
    speak(day)
    speak(month)
    speak(year)

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


if __name__ =="__main__": #Implementing the main function
    wishMe()
    
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Going Offline")
            quit()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary (query, sentences = 2)
            speak(result)
        elif "search in chrome" in query:
            speak("What should I search for?")
            chromepath = "C:/Users/DOLPHIN/AppData/Local/Google/Chrome/Application/chrome.exe %s"
            
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")



# takeCommand()



# time()
# date()

# speak("Hello World! I am JARVIS and I am here to serve Mehedy.")


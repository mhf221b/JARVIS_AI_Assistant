import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 175 #I am setting the speed of the voice, 140 means 140 words per minute
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
        speak("Good Morning, Sir!")
    elif(hour>12 and hour<=18 ):
        speak("Good Afternoon, Sir!")
    elif(hour>18 and hour<=23):
        speak("Good Evening, Sir!")
    else:
        speak("Good Night Sir!")
    speak("Hello! JARVIS at your service")
    time()
    date()
    speak("What can I assist you with?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Can't hear")
        return "None"
    return query


takeCommand()
# wishMe()



# time()
# date()

# speak("Hello World! I am JARVIS and I am here to serve Mehedy.")


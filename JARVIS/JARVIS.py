import pyttsx3
import datetime



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 160 #I am setting the speed of the voice, 140 means 140 words per minute
engine.setProperty('rate', newVoiceRate)

def speak(audio): #this function is used for converting text to speech
    engine.say(audio)
    engine.runAndWait()

def time(): #This Function can say what time it is
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)

time()

speak("Hello World! I am JARVIS and I am here to serve Mehedi.")
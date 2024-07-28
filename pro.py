import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import ec
import subprocess
import ctypes
ctypes.windll.user32.LockWorkStation()
subprocess.call('shutdown /s /f /t 0', shell=True)
subprocess.call('shutdown /r /f /t 0', shell=True)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

    

if _name_ == "_main_":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\akash\\OneDrive\\Desktop\\jarvis'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            from playsound import playsound 
            playsound('C:\\Users\\akash\\Downloads')


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\akash\\OneDrive\\Desktop\\jarvis"
            os.startfile(codePath)
            pywhatkit.sendwhatmsg('6207591273','i love you')
        elif 'lock window'in query:
            speak("locking the devices")
            ctypes.window11.user32.Lockworkstation()
            
        elif 'shutdown system' in query:
            speak("hold on sec ! your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
            
        elif "camera" in query or "take a photo"in query:
            ec.capture(0,"jarvis camera " , "img.jpy")
            
        elif"restart" in query:
            subprocess.call("shutdown","/r")
            
        elif"good morning"in query:
            speak("A warm"+query)
            speak("how are you sir")
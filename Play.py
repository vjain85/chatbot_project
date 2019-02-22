from time import ctime
import os
import win32com.client
from win32com.client import constants
from random import randrange
import webbrowser as wb
import speech_recognition as sr
import audio_find as find
import training as tr
import string
check = 0


def speak(audiostring):
    print(audiostring)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audiostring)


def recordAudio():
    # user input ( speech to text )
    r = sr.Recognizer()
    global check
    with sr.Microphone(device_index=1) as source:
        r.energy_threshold = 280
        r.dynamic_energy_ratio = 0.1
        r.phrase_threshold = 0.1
        r.adjust_for_ambient_noise(source,duration=1)
        print("listening....")
        audio = r.listen(source,phrase_time_limit = 3)
    data = ""
    try:
        print("Audio recorded!")
        data = r.recognize_google(audio,language="en-US")
        print("You said: "+data)
        check = 0
    except sr.UnknownValueError:
        speak("Sorry, couldn't understand you!")
        check = check + 1
        if check == 3:
            speak("Good Bye!")
            exit()
    except sr.RequestError as re:
        speak("It seems you are not connected to internet")
        exit()

    return data


def search_data(data):
    if data:
        if "bye" in data or "exit" in data or "fuck off" in data:
            speak("Good bye")
            exit()
        elif "hi" in data or "hello" in data or "hey" in data or "Dexter" in data:
            speak("Hi, how can I help you ?")
        elif "time now" in data or "time please" in data or "tell me the time" in data:
            speak("now the time is"+ ctime())
        elif "your name" in data:
            speak("My name is Dexter 1.0")
        elif "How old are you" in data or "your age" in data:
            speak("I'm way younger than you")
        elif "about yourself" in data or "introduction" in data:
            speak("Hello, My name is Dexter 1.0. I'm your personal assistant. I was created as a minor project.")
        elif "open YouTube" in data:
            speak("opening YouTube")
            wb.open("https://www.youtube.com")
        elif "YouTube" in data:
            speak("what to search")
            query = recordAudio()
            speak("opening youtube")
            wb.open("https://www.youtube.com/results?search_query="+query, new = 0 , autoraise = True)
        elif "WhatsApp" in data:
            speak("opening whatsapp")
            wb.open("https://web.whatsapp.com/", new = 0, autoraise= True)
        elif "mail" in data:
            speak("opening mail")
            wb.open("http://www.gmail.com/")
        elif "your significance" in data:
            speak("ghar say mai nikla tanha akela, saath me mere kaun hai, BOT hai mera")
        elif "Google" in data:
            speak(" what to search")
            term = recordAudio()
            wb.open("http://www.google.com/search?client=firefox-b-d&q="+term)
            speak("Here is what I found on Google")
        elif "calculate" in data:
            problem = data[10:]
            result = str(eval(problem))
            speak(result)
        elif "let's play" in data or "open" in data:
            if "Counter Strike" in data:
                os.startfile("C:\Program Files (x86)\Condition Zero - Xtreme Edition\czero.exe")
                speak("opening counter strike")
        elif "close" in data or "kill" in data:
            if "Counter Strike" in data:
                os.system("TASKKILL /F /IM czero.exe")
                speak("Counter Strike closed!")
        elif "play" in data:
            if "music" in data:
                speak("opening groove music")
                os.system("start mswindowsmusic:")
        elif "check news" in data:
            speak("fetching latest news for you!")
            wb.open("https://m.dailyhunt.in/news/india/english/")
        elif "train yourself" in data or "start training" in data:
            tr.training_start()
        else:
            find.find_text(data)

#initialization...
speak("Welcome back")

while 1:
    data = input()
    #data = recordAudio()
    search_data(data)

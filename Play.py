from time import ctime
import os
import win32com.client
from win32com.client import constants
from random import randrange
import webbrowser as wb
import speech_recognition as sr
import audio_find as find
import training as tr
import jokes as joke
import facts
import string
check = 0
input_mode = 1

# input_mode = 0 for offline mode
# input_mode = 1 for speech to text
# input_mode = 2 for text input in online mode


def speak(audiostring):
    print(audiostring)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audiostring)


def recordAudio():
    # user input ( speech to text )
    r = sr.Recognizer()
    global check
    global input_mode
    with sr.Microphone(device_index=1) as source:
        r.energy_threshold = 280
        r.dynamic_energy_ratio = 0.1
        r.phrase_threshold = 0.1
        r.adjust_for_ambient_noise(source,duration=1)
        speak("say something!")
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
        if check == 2:
            speak("Switch to text mode instead?")
            speak("This require input in textual form!")
            speak("Say yes if ok or say anything else otherwise!")
            response = recordAudio()
            if 'Yes' in response or 'yes' in response:
                input_mode = 2
        if check == 3:
            speak("Good Bye!")
            exit()
    except sr.RequestError as re:
        speak("It seems you are not connected to internet")
        speak("Switch to offline mode instead?")
        speak("This require input in textual form!")
        speak("Press Y for yes and then enter. Press anything else otherwise!")
        response = input()
        if response == 'Y' or response == 'y':
            input_mode = 0
        else:
            speak("Good Bye!")
            exit()

    return data


def search_data(data):
    if data:
        if "bye" in data or "exit" in data or "fuck off" in data:
            speak("Good bye")
            exit()
        elif "hi" in data or "hello" in data or "hey" in data or "hey Dexter" in data:
            speak("Hi, how can I help you ?")
        elif "help" in data:
            speak("Try one of the following:")
            speak("Say: ")
            speak("hello to get response,")
            speak("open youtube, open whatsapp")
            speak("search google")
            speak("Calculate 2+2")
            speak("how is the weather outside")
            speak("introduce yourself")
            speak("Tell me a joke")
            speak("Tell me some interesting facts")
        elif "how's the Josh" in data or "how is the Josh" in data:
            speak("High Sir!")
        elif "time now" in data or "time please" in data or "tell me the time" in data:
            speak("now the time is "+ ctime())
        elif "your name" in data:
            speak("My name is Dexter 1.0")
        elif "joke" in data or "Joke" in data:
            speak("Yup! One of the interesting jokes I remember is ")
            joke.telljoke()
        elif "fact" in data or "Fact" in data:
            speak("One of the interesting facts I remember is ")
            facts.tellFact()
        elif "How old are you" in data or "your age" in data:
            speak("I don't remember the exact day I born, but I can say I'm way younger than you")
        elif "about yourself" in data or "introduction" in data or "introduce yourself" in data:
            speak("Hello, My name is Dexter 1.0. I'm your personal assistant. I was created as a minor project. "
                  "My skills are: I can open YouTube for you, tell you the current time, open some of the apps "
                  "installed on this pc, do arithmetic calculations, get you updated on the current activities "
                  "running across the world.")
            speak("And most importantly, I give my best when it comes to entertain you.")
            speak("My best part is, 'I never stop learning!'")
        elif "weather" in data:
            speak("let's see what google says about current weather")
            wb.open("http://www.google.com/search?client=firefox-b-d&q=" + data)
        # open commands...

        elif "open" in data and "YouTube" in data:
            if input_mode:
                speak("opening YouTube")
                wb.open("https://www.youtube.com",autoraise=True)
            else:
                speak("Sorry! This can not be done in offline mode")
        elif "open Facebook" in data:
            if input_mode:
                speak("opening facebook")
                wb.open("https://www.facebook.com",autoraise=True)
            else:
                speak("Sorry! This can not be done in offline mode")
        elif "open WhatsApp" in data:
            if input_mode:
                speak("opening whatsapp")
                wb.open("https://web.whatsapp.com/", new=0, autoraise=True)
            else:
                speak("Sorry! This can not be done in offline mode")
        elif "mail" in data:
            speak("opening mail")
            os.system("start outlookmail:")
        elif "YouTube" in data:
            if input_mode == 1:
                speak("what to search")
                query = recordAudio()
                speak("opening youtube")
                wb.open("https://www.youtube.com/results?search_query="+query, new = 0 , autoraise = True)
            elif input_mode == 2:
                speak("what to search")
                query = input()
                speak("opening youtube")
                wb.open("https://www.youtube.com/results?search_query=" + query, new=0, autoraise=True)
            else:
                speak("Sorry! This can not be done in offline mode")
        elif "your significance" in data:
            speak("ghar say mai nikla. tanha akela? saath me mere kaun hai. BOT hai mera?")
        elif "Google" in data:
            if input_mode == 1:
                speak(" what to search")
                term = recordAudio()
                wb.open("http://www.google.com/search?client=firefox-b-d&q="+term,autoraise=True)
                speak("Here is what I found on Google")
            elif input_mode == 2:
                speak("what to search")
                term = input()
                wb.open("http://www.google.com/search?client=firefox-b-d&q=" + term,autoraise=True)
                speak("Here is what I found on Google")
            else:
                speak("Sorry! This can not be done in offline mode")

        # calculate commands...

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
            elif "music" in data:
                os.system("TASKKILL /F /IM mswindowsmusic:")
        elif "play" in data:
            if "music" in data:
                speak("opening groove music")
                os.system("start mswindowsmusic:")
        elif "check news" in data:
            if input_mode == 1 or input_mode == 2:
                speak("fetching latest news for you!")
                wb.open("https://m.dailyhunt.in/news/india/english/")
            else:
                speak("Sorry! This can not be done in offline mode")
        elif "train yourself" in data or "start training" in data:
            tr.training_start()
        else:
            find.find_text(data)

#initialization...
speak("Welcome back")

while 1:
    if input_mode == 1:
        data = recordAudio()
    else:
        data = input()
    search_data(data)

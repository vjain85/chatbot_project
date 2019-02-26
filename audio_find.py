import re
import os
import sqlite3
from random import randrange
from string import punctuation
from collections import Counter
from win32com.client import constants
import win32com.client
import webbrowser as wb

# initialize the connecion to the database

connection = sqlite3.connect("training_data.db")
cursor = connection.cursor()

# create the tables needed by the program

create_table_request_list = [
    'CREATE TABLE words(word TEXT UNIQUE)',
    'CREATE TABLE sentences(Question TEXT UNIQUE,Answer TEXT)'
]

for create_table_request in create_table_request_list:
    try:
        cursor.execute(create_table_request)
    except:
        pass


def speak(audioString):
    print("B: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)


def find_text(string_found):
    rows = cursor.execute("SELECT Answer FROM sentences WHERE Question= '"+string_found[1:]+"'")
    for row in rows:
        #print(row[0])
        if(row[0]):
            speak(row[0])
            return
    rows1 = cursor.execute("SELECT Answer FROM sentences WHERE Question like '%"+string_found[1:]+"%'")
    for row in rows1:
        #print(row[0])
        if(row[0]):
            speak(row[0])
            return
    wb.open("http://www.google.com/search?client=firefox-b-d&q="+string_found)
    speak("Here's what I found on google")
    return


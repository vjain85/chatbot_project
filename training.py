import time
from time import ctime
import os
import sqlite3
from random import randrange
from string import punctuation
from collections import Counter
import win32com.client
from win32com.client import constants

# creating the tables needed by the program

create_table_request_list = [
    "CREATE TABLE words(word TEXT UNIQUE)",
    "CREATE TABLE sentence(question TEXT UNIQUE,answer TEXT)"
]


def speak(audioString):
    print("B: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)

def training_start():
    # initialize the connection to the database
    connection = sqlite3.connect("training_data.db")
    cursor = connection.cursor()

    for create_table_request in create_table_request_list:
        try:
            cursor.execute(create_table_request)
        except:
            pass

    speak("wait while training")
    filenew = "update.txt"
    f = open(filenew,"r+")
    ques = []
    ans = []
    que_status = 1

    while 1:
        lines = f.readlines()
        if not lines:
            break
        for line in lines:
            if "Q:" in line:
                ques = line[3:]
                que_status = 1
            elif "A:" in line and que_status == 1:
                ans = line[3:]
                que_status = 0
                print("Q: "+ques)
                print("A: "+ans)
                cursor.execute("INSERT or REPLACE INTO sentence VALUES(?,?)",(ques,ans))
            else:
                que_status = 0
    f.close()
    connection.commit()
    speak("Training of current data completed")


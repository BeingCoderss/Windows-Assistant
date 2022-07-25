# Importing Libraries
import datetime
import pyttsx3
import pywhatkit
import webbrowser
import pyjokes
import os
import random
from tkinter import *

import speech_recognition

# Initializing Assistance Voice
voice = pyttsx3.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)


# Greeting User
def welcome():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        pyttsx3.speak('Good Morning Sir')
    elif 12 <= hour < 18:
        pyttsx3.speak('Good Afternoon Sir!')
    else:
        pyttsx3.speak('Good Evening Sir!')
    pyttsx3.speak('I am your windows assistant, how may I help you?')


# Taking Command from the User
def inputs():


    global output
    recog = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recog.pause_threshold = 0.6
        sound = recog.listen(mic)
    try:
        output = recog.recognize_google(sound, language='en-in')
    except Exception:
        return "None"
    return output


# Function for whatsapp scheduler with GUI
def whatsapp():
    window = Tk()
    window.title("Whatsapp Scheduler")
    window.geometry('500x500')
    window.configure(bg='black')
    Label(window, text="Whatsapp Message\nScheduler", font="algerian 22 bold", bg='OrangeRed1').pack()
    Label(window, text="Enter Your Message:", font='arial 15 bold', fg='white', bg='black').place(x=50, y=100)
    Label(window, text="Number:", font='arial 15 bold', fg='white', bg='black').place(x=50, y=190)
    Label(window, text="Time(Hour):", font='arial 15 bold', fg='white', bg='black').place(x=50, y=240)
    Label(window, text="24 Hour Format", font='arial 8 bold', fg='white', bg='black').place(x=50, y=270)
    Label(window, text="Time(Min.):", font='arial 15 bold', fg='white', bg='black').place(x=50, y=290)
    entry1 = Entry(window, textvariable=StringVar(), font='arial 16')
    entry2 = Entry(window, textvariable=StringVar(), font='arial 16')
    entry3 = Entry(window, textvariable=StringVar(), font='arial 16')
    entry4 = Entry(window, textvariable=StringVar(), font='arial 16')
    entry1.place(x=50, y=140, width=420, height=35)
    entry2.place(x=220, y=190, width=250, height=35)
    entry3.place(x=220, y=240, width=250, height=35)
    entry4.place(x=220, y=290, width=250, height=35)

    def message():
        entry01 = entry1.get()
        entry02 = entry2.get()
        number = '+91 ' + entry02
        entry03 = entry3.get()
        entry04 = entry4.get()
        pywhatkit.sendwhatmsg(number, entry01, int(entry03), int(entry04), wait_time=10)
        window.destroy()

    Button(window, text='Done', font='arial 12 bold', width='10', bg='lightgreen', command=message).place(x=200, y=370)
    Button(window, text='Discard', font='arial 12 bold', width='10', bg='red', command=window.destroy).place(x=200,
                                                                                                             y=420)
    window.mainloop()


welcome()
while True:
    # command = input()
    command = inputs().lower()
    print(command)

    # if user asks for date
    if 'date' in command:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        pyttsx3.speak(f"Sir, the date is {date}")

    # if user asks for time
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        pyttsx3.speak(f"Sir, the time is {time}")

    # if user wants something to play on YouTube
    elif ('random' in command) or ('youtube video' in command):
        pyttsx3.speak("What would you like to be played on You tube?")
        recog = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            recog.pause_threshold = 0.6
            sound = recog.listen(mic)
            output = recog.recognize_google(sound, language='en-in')
            print(output)
        pywhatkit.playonyt(output)

    # if user commands to open YouTube
    elif 'youtube' in command:
        pyttsx3.speak('opening youtube')
        webbrowser.open('youtube.com')

    # if user commands to open BlackBoard
    elif 'blackboard' in command:
        pyttsx3.speak('opening blackboard')
        webbrowser.open('https://cuchd.blackboard.com')

    # if user commands to open Google
    elif 'google' in command:
        pyttsx3.speak('opening google')
        webbrowser.open('google.com')

    # if user commands to open Google Chrome application
    elif ('open chrome' in command) or ('chrome' in command):
        pyttsx3.speak('opening Google chrome')
        os.startfile(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome")

    # if user commands to open Visual Studio Code
    elif ('open code' in command) or ('vs code' in command) or ('code' in command):
        pyttsx3.speak('opening vs code')
        os.startfile(
            r"C:\\Users\\Rituraj\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio "
            r"Code\\Visual Studio Code")

    # if user wants to open Notepad
    elif 'notepad' in command:
        pyttsx3.speak('Opening Notepad')
        os.system('Notepad')

    # if user asks for a joke
    elif ('joke' in command) or ('funny' in command) or ('jokes' in command):
        pyttsx3.speak(pyjokes.get_joke())

    # if user wants to schedule a message on whatsapp
    elif ('message' in command) or ('whatsapp' in command):
        whatsapp()

    # if user wants to search anything on browser
    elif ('what' in command) or ('why' in command) or ('who' in command) or ('search' in command):
        pyttsx3.speak('Searching')
        pywhatkit.search(command)

    # if user asks to play music
    elif ('play music' in command) or ('music' in command):
        music_dir = "D:\\BE\\B E Courses\\4th Semester\\Minor Project - I\\Music"
        files = os.listdir(music_dir)
        music = random.choice(files)
        os.startfile(os.path.join(music_dir, music))

    # if user wants to take notes on notepad
    elif ('take notes' in command) or ('notes' in command) or ('note' in command):
        f = open('notes.txt', "a")
        pyttsx3.speak('What would you like to be noted down.')
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            audio = r.listen(source)
            content = r.recognize_google(audio, language='en-in')
        f.write(content)
        f.write('\n\n')
        f.close()

    # if user commands to restart the system
    elif 'restart' in command:
        os.system("shutdown /r /t 1")

    # if user commands to shut down the system
    elif ('shutdown' in command) or ('shut down' in command):
        os.system("shutdown /s /t 1")

    elif 'bye' in command:
        pyttsx3.speak("Hava a nice day!")
        exit()
    else:
        pyttsx3.speak('Sorry sir! I did not recognized your voice, please speak.')

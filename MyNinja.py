import datetime
#from selenium import webdriver # to control browser operations 
import os
import random
import re
import smtplib
import tkinter
import webbrowser as wb
from random import randrange
from tkinter import *
from tkinter import ttk

import psutil  # pip install psutil
import pyautogui  # pip install pyautogui
import pyjokes  # pip install pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia

dir(sr)

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak('The Current Time is')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('The Current date is')
    speak(date)
    speak('month is')
    speak(month)
    speak('year is')
    speak(year)


def wishme():
    
    speak('Welcome Back omar!')
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good Morning omar!')
    elif hour > 12 and hour<18:
        speak('Good Afternoon omar!')
    elif hour >=18 and hour<24:
        speak('Good Evening omar!')
    else:
        speak('Good Night omar!')
    speak('Ninja is in your Service... Say How can I help..?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #speak("")
        print("Say something!")
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print('Recognaizing....')
        query = r.recognize_google(audio ,language='en-in')
        
        speak("you say "+query)
        
        print(query)
    except Exception as e:
        print(e)
        speak("Say That Again Please....!")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('','')
    server.sendmail('',to,content)
    server.close()

def screenShoot():
    img = pyautogui.screenshot()
    num = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    foo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    x = random.choice(foo)
    y = random.choice(num)
    filename = str(x)+str(y)+'.png'
    img.save("F:\\Job\\ai\\gui\\screenshot\\"+filename)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU percentage is...' + usage)
    print(usage)
    battary = psutil.sensors_battery()
    speak('Battary percentage is...')
    speak(battary.percent)
    print(battary.percent)

def jokes():
    speak(pyjokes.get_joke())


def mymain():
    
    wishme()
    while True:
        query = takeCommand().lower()      
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak('what should I say?')
                content = takeCommand()
                to = ''
                sendEmail(to,content)
                speak("Email Has been sent!")
            except Exception as e:
                print(e)
                speak("Unable To Send Your Email Try again")
        elif "search in web" in query:
            speak("what should I search ?")
            path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            search = takeCommand().lower() 
            wb.register('firefox',None,wb.BackgroundBrowser(path))
            wb.get('firefox').open_new_tab('https://www.'+search+'.com')
            speak("opening Firefox")
        elif "how are you" in query:
            speak("I'm Fine My Friend Thank You..")  
        elif "your name" in query:
            speak("My Name is Ninja...")  
        elif "your job" in query:
            speak("I'm personal assistance....assists you with their daily personal tasks")  
        elif "my name" in query:
            speak("Your name is omar... the developer who create me..")       
        elif "human" in query:
            speak("No I'm Nothing.... I'm AI System")          
        elif "log out" in query:
            os.system("shutdown -l")
            speak("Signing Out")
            quit()
        elif "shut down" in query:
            os.system("shutdown /s /t 1")
            speak("Shutdown Computer")
            quit()
        elif "restart" in query:
            os.system("shutdown /r /t 1")
            speak("restart Computer")
            quit()
        elif "play songs" in query:
            songs_dir = "F:\\Audio"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
            speak("Opening musics")
        elif "remember" in query:
            speak("What should i remember?")
            data = takeCommand().strip().upper()
            speak("you said me to remember"+ data)
            r = open('gui\\data.txt','w')
            r.write(str(data))
            r.close()
        elif "reminder" in query:
            r = open('gui\\data.txt','r')
            speak("you said me to remind you about.."+ r.read())
        elif "screenshot" in query:
            screenShoot()
            speak("Screenshot Saved..")
        elif ("cpu") in query:
            cpu()
        elif ("battery") in query:
            cpu()
        elif ("joke") in query:
            jokes()
        elif "go to hell" in query:
            speak("Goodbye My Friend... see you again soon...")
            quit()

app = Tk() #Create window object
app.title('Ninja')# Title 
app.geometry('640x640')# size of screen 



background_image = PhotoImage(file="F:\\Job\\ai\\gui\\giphy.gif", format="gif -index 0")

background = Label(app, image=background_image, bd=0)
#background.pack()
background.place(x=0, y=0, relwidth=1, relheight=1)
#part 
 

B = tkinter.Button(app, text ="Click To Talk To Ninja ", font ='50',background = 'black',  foreground = "white",command = mymain,bd=5,justify='center',width='28',highlightcolor='red')
B.grid(row = 0, column = 3, padx = 100) 
B.pack(side = BOTTOM, pady = 30)

app.mainloop()# start program 

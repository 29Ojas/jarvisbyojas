import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
from requests import get
import smtplib
import random
import pywhatkit as kit
import time
import pyjokes
import pyautogui
import requests
import cv2
import sys
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('wadhwa123free@gmail.com', '1732251633')
    server.sendmail('wadhwa123amit@gmail.com', to, content)
    server.close()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Takemanager()


    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text


    def Takemanager(self):
        wishMe()
        while True:
            # if 1:

            # Logic for executing tasks based on query
            self.query = self.takeCommand()
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                speak("Opening youtube sir")
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                speak("Opening google sir")
                webbrowser.open("google.com")

            elif 'open crickbuzz' in self.query:
                speak("Opening crickbuzz sir")
                webbrowser.open("https://www.cricbuzz.com/")

            elif 'open hotstar' in self.query:
                speak("Opening hotstar sir")
                webbrowser.open("hotstar.com")

            elif 'open sony liv' in self.query:
                speak("Opening sonyliv sir")
                webbrowser.open("sonyliv.com")
            elif 'open stackoverflow' in self.query:
                speak("Opening stackoverflock sir")
                webbrowser.open("stackoverflow.com")

            elif 'play my music' in self.query:
                speak("Playing music sir")
                webbrowser.open("https://www.youtube.com/watch?v=8vKs_pelX10")

            elif 'open amazon' in self.query:
                speak("Opening amazon sir")
                webbrowser.open("amazon.com")

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:
                speak("Opening vs code sir")
                self.codePath = "C:\\Users\\wadhw\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(self.codePath)

            elif 'open whatsapp' in self.query:
                 speak("Opening whatsapp sir")
                 webbrowser.open("https://web.whatsapp.com/")

            elif 'open code with harry channel' in self.query:
                speak("Opening sir")
                webbrowser.open(
                    "https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")

            elif 'open amazon' in self.query:
                speak("Opening amazon sir")
                webbrowser.open("amazon.com")

            elif 'open github' in self.query:
                speak("Opening your github account sir")
                webbrowser.open("github.com")

            elif 'open flappy bird' in self.query:
                speak("Opening sir")
                self.codePath = "D:\\Python\\Pygame\\Flappy bird"
                os.startfile(self.codePath)

            elif 'open download menu' in self.query:
                speak("Opening sir")
                self.codePath = "D:\\Python\\Pygame\\Snakes"
                os.startfile(self.codePath)

            elif 'send email' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "wadhwa123amit@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")

            elif 'exit' in self.query:
                speak("Ok bye sir see you again tommorrow!")
                exit()

            elif 'in youtube' in self.query:
                speak('Searching Youtube...')
                webbrowser.open(
                    "https://www.youtube.com/results?search_query=" + self.query)

            elif "in google" in self.query:
                speak("Searching Google...")
                webbrowser.open(
                "https://www.google.com/search?q=" + self.query)

            elif "play music" in self.query:
                self.codePath = "D:\\Python\\Jarvis\\play1.mp3"
                os.startfile(self.codePath)

            elif 'open facebook' in self.query:
                speak("Opening facebook sir")
                webbrowser.open("facebook.com")

            elif 'open instagram' in self.query:
                speak("Opening instagram sir")
                webbrowser.open("instagram.com")

            elif 'shutdown computer' in self.query:
                speak("Ok sir shutdowning...")
                os.system('shutdown /s /t 1')
                speak("Thank your sir for using me , Have a Nice day ahead!")
                exit()

            elif 'restart computer' in self.query:
                speak("Ok sir restarting...")
                os.system('shutdown /r /t 5')
                speak("Thank your sir for using me , Have a Nice day ahead!")
                exit()

            elif 'sleep computer' in self.query:
                speak("Ok sir...")
                os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
                speak("Thank your sir for using me , Have a Nice day ahead!")
                exit()

            elif "how are you" in self.query:
                speak("I am fine sir!")

            elif 'open sonyliv' in self.query:
                speak('opening sonyliv sir')
                webbrowser.open('sonyliv.com')

            elif "open notepad" in self.query:
                speak("Opening notepad sir")
                self.path = "C:\\WINDOWS\\system32\\notepad"
                os.startfile(self.path)

            elif "open command prompt" in self.query:
                print("Opening sir")
                os.system("start cmd")

            elif "play a song of your choice" in self.query:
                speak("Playing sir")
                self.music_dir = "D:\\Songs"
                self.songs = os.listdir(self.music_dir)
                self.rd = random.choice(self.songs)
                os.startfile(os.path.join(self.music_dir, self.rd))

            elif "good choice" in self.query:
                speak("Thankyou sir always here for your sir")

            elif "send message in whatsapp" in self.query:
                speak("What should I say")
                self.cm = self.takeCommand().lower()
                n1 = int(datetime.datetime.now().hour)
                n2 = int(datetime.datetime.now().minute)
                n3 = n2 + 2
                kit.sendwhatmsg("+919896341633", str(self.cm), n1, n3)

            elif "remember that" in self.query:
                speak("what should I say")
                fi = self.takeCommand().lower()
                with open('file.txt', 'w') as f:
                    a = f.write(str(fi))

            elif "what we are doing" in self.query:
                with open('file.txt') as f:
                    b = f.read()
                    speak("sir" + b)

            elif "close notepad" in self.query:
                speak("Closing notepad, sir!")
                os.system("taskkill /f /im notepad.exe")

            elif "close code" in self.query:
                speak("Closing code, sir!")
                os.system("taskkill /f /im Code.exe")

            elif "close" in self.query:
                speak("Done, sir!")
                os.system("taskkill /f /im msedge.exe")

            elif "set alarm" in self.query:
                speak("Speak your hours")
                n1 = int(self.takeCommand())
                speak("Speak your minutes")
                n2 = int(self.takeCommand())
                n3 = int(datetime.datetime.now().hour)
                n4 = int(datetime.datetime.now().minute)
                while True:
                    if n3 == n1 and n4 == n2:
                        s = "D:\\Songs\\play2.mp3"
                        os.startfile(s)
                        break
                    else:
                        n3 = int(datetime.datetime.now().hour)
                        n4 = int(datetime.datetime.now().minute)

            elif "i am going" in self.query:
                speak("Where are you going sir")

            elif "sleep" in self.query:
                n = False
                while n == True:
                    time.sleep(500)
            elif "wakeup" in self.query:
                speak("I am always here for you sir")

            elif "hello" in self.query:
                speak("Hello sir how can i help you")

            elif "tell me any joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "change windows" in self.query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')

            elif 'where i am' in self.query:
                try:
                    speak("wait sir let me check")
                    ipAdd = requests.get("https://api.ipify.org.").text
                    print(ipAdd)
                    url = 'https:\\get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['City']
                    country = geo_data['Country']
                    speak(
                        f"I am not sure but I think we are in {city} city of {country} country")

                except Exception as e:
                    speak("Sorry i dont found due to the network issue")
                    pass

            elif "open my tuition" in self.query:
                speak("Opening sir")
                webbrowser.open(
                    "https://unacademy.com/goal/cbse-class-8/TICPI")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = self.takeCommand()
                timing = timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')

                time.sleep(timing)
                speak('Your time has been finished sir')

            elif "take screenshot" in self.query:
                speak("Tell me the name for your screenshot")
                self.name = self.takeCommand().lower()
                speak("Taking screen shot sir")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{self.name}.png")
                speak("I am done sir, screenshot is saved in your pc")
            elif "thank you" in self.query:
                speak("Its my pleasure sir")
            elif "do calculations" in self.query:
                try:
                    speak("Speak your first number sir")
                    n1 = int(self.takeCommand())
                    speak("What do you want to do")
                    s = self.takeCommand().lower()
                    speak("Speak your second number sir")
                    n2 = int(self.takeCommand())
                
                    if s == "plus":
                        speak(n1+n2)
                        print(n1+n2)
                    elif s == "minus":
                        speak(n1-n2)
                        print(n1-n2)
                    elif s == "product":
                        speak(n1*n2)
                        print(n1*n2)
                    elif s == "divide":
                        speak(n1/n2)
                        print(n1/2)
                    else:
                        speak("You speak it wrong")

                except Exception as e:
                    speak("Try again...")


            elif "hide all the files" in self.query:
                os.system("attrib +h /s /d")
                speak("sir all the files are hide now")
            elif "show all the files" in self.query:
                os.system("attrib -h /s /d")
                speak("sir all the files are visible now")

startManager = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)


    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/wadhw/Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/wadhw/Downloads/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startManager.start()


    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
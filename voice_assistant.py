import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
import subprocess
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import re 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            speak("Good Morning Sir !")

        elif hour>= 12 and hour<18:
            speak("Good Afternoon Sir !")  

        else:
            speak("Good Evening Sir !") 

        assname =("FRIDAY 1 POINT 0")
        speak("I am your Assistant")
        speak(assname)
def UserName():
        speak("What should I call you sir?")
        username= takeCommand()
        speak("Welcome Mister")
        speak(username)
        columns = shutil.get_terminal_size().columns
        print("Welcome Mr.",username.center(columns))
        speak("How can i Help you, Sir")

def takeCommand():
         r = sr.Recognizer()
         with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

            try:
                print("Recognizing...")   
                query = r.recognize_google(audio, language ='en-in')
                print(f"User said: {query}\n")

            except Exception as e:
                print(e)   
                print("Unable to Recognize your voice.") 
                return "None"

            return query

if __name__ =='__main__':
        clear= lambda:os.system('cls')
        clear()
        wishMe()
        UserName()

        while True:
            query= takeCommand().lower()

            if 'wikipedia' in query:
                speak("Searching Wikipedia")
                query=query.replace("Wikipedia","")
                results=wikipedia.summary(query,sentences='4')
                speak("According to Wikipedia: ")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                speak("Opening Youtube")
                webbrowser.open('youtube.com')
            elif 'open google' in query:
                speak("Redirecting to google")
                webbrowser.open('google.com')
            elif 'the time' in query:
                time_now=datetime.datetime.now()
                strtime=time_now.strftime("%H:%M:%S")
                speak(f"Sir, the time is {strtime}")
            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you sir?")
            elif 'fine' in query or 'good' in query:
                speak("Good to know")
            elif 'who made you' in query:
                speak("I am programmed by Mister Stark for your assistance.")
            elif 'search' in query or 'play' in query:
                query=query.replace("search", "")
                query=query.replace("play","'")
                webbrowser.open(query)
            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.com / maps / place/" + location + "") 
            elif 'friday' in query:
                wishMe()
                speak('Friday 1 point 0 at your service Mister')
                speak(assname)
            elif "weather" in query:

                api_key = "533bf5c80206941a24a3263719543b8e"
                base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                speak(" City name ")
                print("City name : ")
                city_name = takeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()

                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))

                else:
                    speak(" City Not Found ")
            elif "greatest of all time" in query:
                speak("Lionel Messi is the greatest player of all time")
            elif "exit" in query:
                speak("Thankyou! talk to you soon.")
                exit()
            elif "open" in query:
                query=query.replace("open","")
                webbrowser.open(query)
            elif "joke" in query:
                speak(pyjokes.get_joke())
            elif "netflix" in query:
                print("Opening netflix")
                speak("Opening Netflix")
                os.startfile("netflix")
            elif "amazon prime" in query:
                speak("Redirecting to amazon prime video")
                webbrowser.open('primevideo.com')
            elif "hotstar" in query:
                speak("Redirecting to hotstar")
                webbrowser.open('hotstar.com')
            
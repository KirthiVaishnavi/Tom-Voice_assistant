# -*- coding: utf-8 -*-
"""
Created on Sun May 16 20:26:15 2021

"""
from platform import uname
from tkinter import *
import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import shutil
from twilio.rest import Client


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def click():
    b1.config(text="Listening...")
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning !")
    
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon !")
    
        else:
            speak("Good Evening !")
    
        assname = ("Tom")
        speak("I am your Assistant")
        speak(assname)
    
    
    def usrname():
        speak("What should i call you?")
        uname = takeCommand()
        speak("Welcome")
        speak(uname)
        columns = shutil.get_terminal_size().columns
    
        print("#####################".center(columns))
        print("Welcome ", uname.center(columns))
        print("#####################".center(columns))
    
        speak("How can i Help you?")
    
    
    def takeCommand():
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
            print(e)
            print("Unable to Recognize your voice.")
            return "None"
    
        return query
    
    
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
    
        # Enable low security in gmail
        server.login('charanh117@gmail.com', '8328175557')
        server.sendmail('charanh117@gmail.com', to, content)
        server.close()
    
    
    if __name__ == '__main__':
        clear = lambda: os.system('cls')
    
        clear()
        wishMe()
        usrname()
    
        while True:
    
            query = takeCommand().lower()
    
            # All the commands said by user will be
            # stored here in 'query' and will be
            # converted to lower case for easily
            # recognition of command
            if 'from wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif "open wikipedia" in query:
                speak("Here you go to Wikipedia\n")
                webbrowser.open("wikipedia.com")
    
            elif 'open youtube' in query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")
    
            elif 'open google' in query:
                speak("Here you go to Google\n")
                webbrowser.open("google.com")
    
            elif 'open stackoverflow' in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")
                
            elif 'open gmail' in query:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime('%H:%M %S')
                speak(f"Current time is {strTime}")
    
            elif 'email to charan' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "keerthiyshu9@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
    
            elif 'send a mail' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("whom should i send")
                    to = input()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
    
            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you")
    
            elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
    
            elif "change my name to" in query:
                query = query.replace("change my name to", "")
                uname = query
    
            elif "change name" in query:
                speak("What would you like to call me? ")
                assname = takeCommand()
                speak("Thanks for naming me")
    
            elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me Tom")
                print("My friends call me Tom")
    
            elif 'exit' in query:
                speak("Thanks for giving me your time")
                exit()
    
            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Vaishnavi,Mohsina and Haricharan.")
    
            elif 'joke' in query:
                speak(pyjokes.get_joke())
    
            
            elif 'search' in query or 'play' in query:
    
                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)
    
            elif "who i am" in query:
                speak("If you talk then definately your human.")
    
            elif "who are you" in query:
                speak("I am your virtual assistant")
    
            elif 'reason for you' in query:
                speak("I was created as a Minor project")
    
            elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
                speak("Background changed succesfully")
    
            elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)   
               
    
            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
    
            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
    
            elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")
    
            elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop TOM from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)
    
            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location + "")
    
            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])
    
            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")
    
            elif "log off" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])
    
            elif "write a note" in query:
                speak("What should i write?")
                note = takeCommand()
                file = open(r'Tom.txt', 'w')
                speak("Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H: %M: %S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
    
            elif "show note" in query or "open note" in query:
                speak("Showing Notes")
                file = open(r"Tom.txt", "r")
                print(file.read())
                speak(file.read(6))
    
            # NPPR9-FWDCX-D2C8J-H872K-2YT43
            elif "Tom" in query:
    
                wishMe()
                speak("Tom at your service")
    
            elif 'current weather' in query:
                search_term = query.split("for")[-1]
                url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
                webbrowser.get().open(url)
                speak("Here is what I found for on google")
        
            elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
    
                message = client.messages \
                    .create(
                    body=takeCommand(),
                    from_='Sender No',
                    to='Receiver No'
                )
    
                print(message.sid)
     
    
            elif "Good Morning" in query:
                speak("A warm" + query)
                speak("How are you")
                speak(uname)
    
            # most asked question from google Assistant
            elif "will you be my bf" in query:
                speak("I'm not sure about, may be you should give me some time")
    
            elif "how are you" in query:
                speak("I'm fine, thanks for asking")
    
            elif "i love you" in query:
                speak("It's hard to understand")

            elif "add" in query:
                sum=query.replace("add","").replace("plus","+")
                ans=eval(sum)
                speak(ans)

            elif "subtract" in query:
                sub=query.replace("subtract","").replace("minus","-")
                ans=eval(sub)
                speak(ans)

            elif "multiply" in query:
                star=query.replace("multiply","").replace("star","*")
                ans=eval(star)
                speak(ans)

            elif "divide" in query:
                By=query.replace("divide","").replace("by","/")
                ans=eval(By)
                speak(ans)


   
def shut():
        #bids the user goodbye and quits
        pyttsx3.speak("Thanks for giving me your time")
        exit()
root=Tk()
root.geometry("800x1000")
root.configure(bg="#EEE8AA")
root.title("VOICE ASSISTANT")

label1=Label(root,text="TOM",font=("Arial Bold",60),bg="#EEE8AA",fg="Black").pack(padx=10,pady=30)

canvas=Canvas(root,width=500,height=500,bg="#EEE8AA")
img=PhotoImage(file="va-icon.jpg")
canvas.create_image(250,250,anchor=CENTER,image=img)
canvas.pack(padx=10,pady=30)

global b1
b1=Button(root,text="Tap to Speak",bg="Black",fg="white",font='bold',width=30, command=click)
b1.pack(padx=10,pady=10)

b2=Button(root,text="Exit",bg="Black",fg="white",font='bold',width=30, command=shut)
b2.pack()


root.mainloop()

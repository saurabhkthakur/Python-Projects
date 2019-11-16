import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import urllib.request
import urllib.parse
import re
from googlesearch import search


engine = pyttsx3.init('sapi5') # to take inbuilt windows api for voices
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning")
        
    elif hour>=12 and hour <18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    speak('how may i help you sir i am always there for u . Hope u have a good day')    
 

def takeCommand():
    #it takes microphone input from user and cinvert it into strings    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognisinh...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("say that again please..")
        return 'None'
    return query

def sendEmail(to , content):
    server  = smyplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('thakurksaurabh96@gmail.com','Thakur@447')
    server.sendmail('thakurksaurabh96@gmail.com', to,content)
    server.close()



if __name__ == "__main__":
    speak("this is going to be awesome batman")
    
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching wikipedia ...')
            query =query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        
        # search anythoing in youtube
        elif 'play from youtube' in query: 
            speak('What do you want to search in youtube')
            youtube_query = takeCommand()
            query_string = urllib.parse.urlencode({"search_query" : youtube_query}) 
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string) 
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            print("http://www.youtube.com/watch?v=" + search_results[0])
            webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
            
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
      
        elif 'search google' in query:
            speak('What do you want to search')
            G_Search = takeCommand()
            url = "https://www.google.co.in/search?q=" +(str(G_Search))+ "&oq="+(str(G_Search))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
            webbrowser.open_new(url)
         
            
        elif 'open website' in query:
            speak('Which website do you want to visit')
            Web_search = takeCommand()
            Website=[]
            for url in search(Web_search, tld='com.pk', lang='es', stop=5):
                Website.append(url)
            webbrowser.open(Website[0])
            
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            
        
        elif 'play music from playlist' in query:
            music_dir = 'C:\\Users\\Nandan\\Music'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir ,songs[random.randint(0,len(songs)-1)]))
         
       
        elif 'the time' in query:
            strTime = datetime.datetime.strftime("%H:%M:%S")
            
        
        elif ' send email ' in query:
            
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "thakurksaurabh96@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
                
        
            except Exception as e:
                print(e)
                speak('Email not recognize')
            
            
            
            
        if 'shutdown' in query:
            speak('I am shutting u can call me any time')
            break
        
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import pyjokes
import os
import time
from urllib.request import urlopen
import wolframalpha
from ecapture import ecapture as ec
import subprocess



def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understand")
            speechtx("Not understand")

def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':


    if "khushi" in sptext().lower():
            while True:
                    data1=sptext().lower()

                    if "your name" in data1:
                        name = "my name is khushi"
                        speechtx(name)
               

                    elif "old are you" in data1:
                        age = "i am ten years old"
                        speechtx(age)

                    elif "how are you" in data1:
                        sp= "i am fine"
                        speechtx(sp)

                    elif "who are you" in data1:
                        speechtx("I am your voice assistance")
                  
                    elif "time" in data1:
                        time = datetime.datetime.now().strftime("%I%M%p")
                        speechtx(time)

                    

                    elif "youtube" in data1:
                        webbrowser.open("https://www.youtube.com/")

                    elif "open mail" in data1:
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                        speechtx("Google mail open now")

                    elif "search" in data1:
                        data1=data1.replace("search","")
                        webbrowser.open_new_tab(data1)


                    elif "news" in data1:
                        news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/?from=mdr")
                        speechtx("Here are some headlines from the times of india .Happy reading")
                        

                    elif "camera" in data1:
                        ec.capture(0,"robo s=camera","img.jpg")

                    elif "joke" in data1:
                        joke_1 = pyjokes.get_joke(language="en",category="neutral")
                        print(joke_1)
                        speechtx(joke_1)

                    elif "play song" in data1:
                        add = "C:/Users/Songs"
                        listsong=os.listdir(add)
                        print(listsong)
                        os.startfile(os.path.join(add,listsong[0]))

                    elif "show pictures" in data1:
                        pic="Pictures"
                    
                    elif "wikipedia" in data1:
                        print("Searching wikipedia")
                        results=wikipedia.summary(data1,sentences=3)
                        print("According to wikipedia")
                        print(results)
                        speechtx(results)

                    elif "open map" in data1:
                        speechtx("Opening google map")
                        webbrowser.open("https://maps.google.com/")

                    elif "open google" in data1:
                        speechtx("Opening Google\n")
                        webbrowser.open("https://www.google.com/")

                    elif "log off" in data1 or "sign out" in data1:
                        speechtx("ok,your pc will log off in 10 sec make sure you exit from all applications")
                        subprocess.call(["shutdown","/1"])


                    
                    elif "exit" in data1:
                        speechtx("thank you")
                        break

                    time.sleep(10)

    else:
        print("thanks")
        speechtx("thanks")
    



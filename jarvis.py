import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
# sapi5 gives the inbuilt voices of computer
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Defining speak function to give audio to computer
def speak(audio):
    engine.say(audio)
    # it will say what you have written
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        # Tell about the morning time
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")
        # Tell about the Noon Time
    else:
        speak("Good Evening!")
    speak("I am ZIRA sir. Please tell me How may I Help you?")

def takeCommand():
    # Take command as microsoft input from user and return in the form of string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query + '\n')

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manavahuja274@gmail.com', 'despacito')
    server.sendmail('manavahuja274@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir,The time is: " + strTime)

        elif 'open code' in query:
            codeLocation = "C:\\Program Files\\Jet Brains py\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
            os.startfile(codeLocation)

        elif 'email to manav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "manavahuja274@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry My dear friend,I am not able to send this email!")



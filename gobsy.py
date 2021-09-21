import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Galav sir")
    elif hour>12 and hour<=15:
        speak("Good Afternoon Galav sir")
    elif hour>15 and hour<=22:
        speak("Good Evening Galav sir")
    else:
        speak("Good Night Galav Bhatt sir")
    speak("Hello i am Ms.gobsy! How may i help you sir.")

def takeCommand():
    '''It takes microphone input from the user and return the string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        '''Here we will define the logic for tasks based on the user requirement'''
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)
            speak("anything else you would like to know sir") 
            break

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Okay sir i will open youtube for you.")
            break
        elif 'machine learning' in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU")
            speak("I have opened Master Andrew ng tutorial playlist for you.")
            break
        elif 'google' in query:
            webbrowser.open("google.com")
            speak("I have opened google for you.")
            break
        elif 'stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            speak("I have opened stackoverflow for you.")
            break
        elif 'music' in query:
            music_dir = 'C:\\Users\\Dell\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")
            break
        elif 'open code' in query:
            visual_code_dir = 'C:\\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(visual_code_dir)
            speak("I have opened Visual studio code for you! anything else sir")
            break
        elif 'email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "galav.bhatt2026@gmail.com"
                def sendemail(to,content):
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login('galavbhatt6@gmail.com','............')
                    server.sendmail('galavbhatt6@gmail.com',to,content)
                    server.close()
                print("Email has been sent successfully!")
                speak("Email has been sent successfully!")
        

            except Exception as e:
                speak("Sorry Galav sir i am unable to send the mail!")
                print("Sorry Galav sir i am unable to send the mail!")


        else:
            print("Please Say Something else")
            speak("Please Say Something else")
            break
        



    
            



    
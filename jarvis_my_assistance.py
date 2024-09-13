import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour>12:
        speak("Good Morning shubham sir!")

    elif hour>=12 and hour>18:
        speak("good after noon shubham sir!")

    else:
        speak("Goood morning shubham sir!")

    speak("I am jarvis sir. how may i help you!")
def takeCammand():

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listenig...")
        r.pause_threshold = 2
        r.energy_threshold = 350
        audio = r.listen(source)

    try:
        print("Recognize...")  
        querry = r.recognize_google(audio, language='en-in')
        print(f"shubham_said:n {querry}/n")

    except Exception as e:
        print("Say it again....") 
        return "none"
    return querry 

def sendEmail(to, content):  
    server= smtplib.SMTP("smtp.gamil.com", 587)
    server.ehlo
    server.starttls()
    server.login("shubham99singh11@gmail.com, shubam@123")
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
       query = takeCammand().lower()

       if 'wikipedia'in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query , )
        speak("accourding to wikipedia")
        print(results)
        speak(results) 

       elif 'open google' in query: 
           webbrowser.open("Google.com")

       elif 'open youtube' in query: 
           webbrowser.open("youtub.com")

       elif 'open stack overflow' in query: 
           webbrowser.open("stackoverflow.com")  

       elif ' what is my love name' in query:
          speak(" sir, your love name start from S")
         
       elif ' the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir, the time is{strTime}") 
        
       elif 'email to shubham' in query:
            try:
                 speak("what should i say?")
                 content = takeCammand()
                 to = "shubham99singh11@gmail.com"
                 sendEmail(to, content)
                 speak(" email has been sent")
            except Exception as e:
                print(e)
                speak("sorry, shubham sir!, I am not able to send email at this moment")

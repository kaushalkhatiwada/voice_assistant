
#pip install SpeechRecognition
#pip install pyttsx3
import speech_recognition as sr
import pyttsx3

#Convert Text To Speech with pyttsx3 library
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   #change voice to female

def speak(text): 
    engine.say(text)        #Text that we want to convert to speech
    engine.runAndWait()

#Get Audio From Microphone with speech_recognition library

        #To get my microphone Information
        #for i,j in enumerate(sr.Microphone.list_microphone_names()):
                #print(i,j)         #microphone id 2 in my case
def voicecommand():
    r1 = sr.Recognizer()
    with sr.Microphone(2) as myvoice:   #2 is my microphone ID
        print("Please Set Reminder")
        speak('Please Set Reminder!!')
        print('Listening...')       
        try:
            reminder = r1.recognize_google(r1.listen(myvoice), language="en-US")   #recognize speech using google 
            print(f'Event: {reminder}')
            return reminder
        except sr.UnknownValueError:
            print("Sorry, could not hear you..Bye")
        
def date():
    r2 = sr.Recognizer()
    with sr.Microphone(2) as myvoice:   #2 is my microphone ID
        print('Please Set Date')
        speak('Please Set Date ')
        print ('Date Format: May 3rd')
        print('Listening...')      
        try:
            dates = r2.recognize_google(r2.listen(myvoice), language="en-US")
            print(f'Reminder set for {dates}')
            speak(f'Reminder set for {dates}')
            return dates
        except sr.UnknownValueError:
            print("Sorry, could not hear you..Bye")
        
def time():
    r3 = sr.Recognizer()
    with sr.Microphone(2) as myvoice:   #2 is my microphone ID
        print(f"Please Set Time on {dates}")
        speak(f'Please Set Time on {dates}')
        print ('Time Format: 10:30 PM')
        print('Listening...')      
        try:
            times = r3.recognize_google(r3.listen(myvoice), language="en-US")
            return times 
        except sr.UnknownValueError:
            print("Sorry, could not hear you..Bye")

def setreminder():
    with open('reminder.txt',"a") as a:         #Voice commanded reminder converted to text in txt file
        a.write(f"{dates} {times}:> {command}\n")
    print(f'Reminder  is set for {dates} at {times}')
    speak(f'Reminder  is set for {dates} at {times}')
    return

command=voicecommand()
if command is None:
    speak("Sorry Could not hear you.")
else:
    dates = date()
    if dates is None:
        speak("Sorry Could not hear you.")
    else:
        times=time()    
        if times is None:
            speak("Sorry Could not hear you.")
        else:
            setreminder()
        


    



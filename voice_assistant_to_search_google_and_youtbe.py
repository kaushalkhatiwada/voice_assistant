
#pip install SpeechRecognition
#pip install pyttsx3
#pip install webbrowser
import speech_recognition as sr
import pyttsx3
import webbrowser as wb

#Convert Text To Speech with pyttsx3 library
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   #change voice to female

def speak(text): 
    engine.say(text)        #Text that we want to convert to speech
    engine.runAndWait()

#Get Audio From Microphone with speech_recognition library

        #To get my microphone Information
        # for i,j in enumerate(sr.Microphone.list_microphone_names()):
        #     print(i,j)
def voicecommand(): 
    r1 = sr.Recognizer()   
    with sr.Microphone(2) as myvoice:   #2 is my microphone ID
        print("Google or Youtube")
        speak('Google or Youtube')
        print('Listening...')
        audio = r1.listen(myvoice,phrase_time_limit=3)       
        try:
            text = r1.recognize_google(audio)   #recognize speech using google 
            print(f'Command: {text}')
            return text.lower()
        except:
            print("Sorry, could not hear you")
            speak("Sorry, could not hear you")
            return ''          

def youtube(): 
    r2 = sr.Recognizer()
    url="https://www.youtube.com/results?search_query="
    with sr.Microphone(2) as myquery:                   #search query in youtube
        print('Opening Youtube..')
        speak("Opening Youtube...")
        speak('What do you want to watch?')
        audio1=r2.listen(myquery,phrase_time_limit=3)
        try:
            query=r2.recognize_google(audio1)
            print(f'Searching for {query}...')
            wb.open_new(url+query)
            speak(f'Enjoy watching {query}')
        except:
            print("Sorry, could not hear you")
            speak("Sorry, could not hear you")
            return
            
            
def google():
    r3 = sr.Recognizer()
    print('Opening Google..')
    speak('Opening Google..')
    googleurl="https://www.google.com/search?q="
    with sr.Microphone(2) as mysearch:                   #search query in youtube
        speak('What do you want to search?')
        audio2=r3.listen(mysearch,phrase_time_limit=3)
        try:
            search=r3.recognize_google(audio2)
            print(f'Searching for {search}...')
            wb.open_new(googleurl+search)
            speak(f'Search Result for {search}')
        except:
            print("Sorry, could not hear you")
            speak("Sorry, could not hear you")
            return

while True:     
    command = voicecommand()
    if 'youtube' in command:
        youtube()                   #Open youtube.com with 'ok' command
        break

    if 'google' in command:       
        google()                    #Open google.com with 'ok' command    
        break 

    elif 'bye' in command:
        speak('BYE BYE')
        break
    



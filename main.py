import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
 engine.say(text)
 engine.runAndWait()


def take_command():
 try:
    with sr.Microphone() as source:
        print('listening...') #giving indication that voice assistant is listening to you
        voice =  listener.listen(source)
        command =  listener.recognize_google(voice)
        command =  command.lower()
        if 'alexa' in command:
         command = command.replace('alexa', '')
         print(command)

 except:
    pass
 return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is' +time)

    elif 'joke' in command:
        joke= pyjokes.get_joke()
        print(joke)
        talk(joke)  

    elif 'you are intelligent'  in command:
        string='I know, I was born smart'
        print(string)
        talk(string)    

    elif 'who is' or 'what is' in  command:
        item = command.replace('who is' or 'what is', '')
        info = wikipedia.summary(item, 1)
        print(info)
        talk(info)         

    else:
        talk('Sorry, I did not understand you, please repeat')    

while True:
 run_alexa() #calling function       


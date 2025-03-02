import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import screen_brightness_control as screen


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Pineapple is listening...")
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'pineapple' in command:
                command = command.replace('pineapple', '')
                talk(command)
            else:
                talk("Start your command by saying Pineapple")
    except:
        talk("Sorry, I can't hear that.")
    return command

def run_pineapple():
    command = listen()
    print(command)
    if "play" in command:
        song=command.replace("play", "")
        talk("Now playing"+ song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("The time is"+time)

    elif "who is" in command:
        person=command.replace("who is", "")
        info=wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif "what is" in command:
        item=command.replace("what is", "")
        info = wikipedia.summary(item, 1)
        print(info)
        talk(info)
    elif "set brightness to" in command:
        brightness=int(command.replace("set brightness to", ""))
        screen.set_brightness(brightness)
        get=screen.get_brightness()
        talk("Brightness has successfully been set to"+str(brightness))
    elif "thank you" in command:
        talk("Thankyou for using Pineapple")
        return True

    return False


while True:
    if run_pineapple():
        break
































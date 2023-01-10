import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
machine = pyttsx3.init()
def talk(text):
    machine.say(text)
machine.runAndWait()
def input_instruction():
    global instruction


    try:
        with sr.Microphone() as origin:
            print("listening.....")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction= instruction.lower()
            if "Alexa" in instruction:
                instruction = instruction.replace("Alexa"," ")
                print(instruction)
            print(instruction)

    except:
        pass
    return instruction
def play_Alexa():
    instruction= input_instruction()
    print(instruction)
    if "play" in instruction:
        song= instruction.replace("play"," ")
        talk("playing"+ song)
        pywhatkit.playonyt(song)
    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M%P")
        talk("Current time" + time)
    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d /%M /%Y")
        talk("Today's date" + date)
    elif "how are you" in instruction:
        talk("I am fine, how about you?")
    elif "what is your name" in instruction:
        talk("I am Alexa, what can I do for you")
    elif "who is" in instruction:
        human = instruction.replace("who is"," ")
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)
    else:
        talk("please repeat")
    
play_Alexa()

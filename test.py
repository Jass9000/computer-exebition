import pyttsx3
engine = pyttsx3.init()
while True:

    engine.say(input("prompt:"))
    engine.runAndWait()
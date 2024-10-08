import pyttsx3
engine = pyttsx3.init()
while True:
    engine.say("I will speak this text")
    engine.runAndWait()
import pyttsx3
a=pyttsx3.init()
while True:
    x=input()
    if x =="123":
        exit()
    a.say(x)
    a.runAndWait()
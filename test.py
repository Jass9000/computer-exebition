from tkinter import *
import playsound
import time

# Initialize i to track the current question
i = 0
root = Tk()
root.geometry('1200x900+0+0')
root.title('Kaun Banega Crorepati')
root.config(bg='black')

questions_data = [
    {
        "question": "What is the capital of the Indian state of Maharashtra?",
        "options": ["Pune", "Mumbai", "Nashik", "Nagpur"],
        "answer": "Mumbai"
    },
    {
        "question": "The speed of Sound is maximum in which of the following?",
        "options": ["Air at 100°C", "Air at 0°C", "Vaccum", "Same in all"],
        "answer": "Air at 100°C"
    },
    {
        "question": "Which tech giant has developed an AI-powered coding assistant named Studio Bot?",
        "options": ["Microsoft", "Intel", "Google", "Apple"],
        "answer": "Google"
    },
    {
        "question": "Who is the father of Computers?",
        "options": ["James Gosling", "Charles Babbage", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "Charles Babbage"
    }

]


amountimage1 = PhotoImage(file='p1.png')
amountimage2 = PhotoImage(file='p2.png')
amountimage3 = PhotoImage(file='p3.png')
amountimage4 = PhotoImage(file='p4.png')
amountimage5 = PhotoImage(file='p5.png')
amountimage6 = PhotoImage(file='p6.png')
amountimage7 = PhotoImage(file='p7.png')
amountimage8 = PhotoImage(file='p8.png')
amountimage9 = PhotoImage(file='p9.png')
amountimage10 = PhotoImage(file='p10.png')
amountimage11 = PhotoImage(file='p11.png')
amountimage12 = PhotoImage(file='p12.png')
amountimage13 = PhotoImage(file='p13.png')
amountimage14 = PhotoImage(file='p14.png')
amountimage15 = PhotoImage(file='p15.png')
amountimage16 = PhotoImage(file='p16.png')

global amountImages 
amountImages=[amountimage1,amountimage2, amountimage3, amountimage4,
    amountimage5, amountimage6, amountimage7, amountimage8,
    amountimage9, amountimage10, amountimage11, amountimage12,
    amountimage13, amountimage14, amountimage15, amountimage16
]


def select(event):
    global i
    a = event.widget
    value = a['text']
    
    # Access current question's answer
    current_question = questions_data[i]
    
    if value == current_question["answer"]:
        playsound.playsound("clap.wav")
        questionArea.delete(1.0, END)
        i += 1  # Move to the next question
        if i < len(questions_data):  # Ensure i doesn't exceed available questions
            next_question = questions_data[i]
            questionArea.insert(END, next_question["question"])
            optionButton1.config(text=next_question["options"][0])
            optionButton2.config(text=next_question["options"][1])
            optionButton3.config(text=next_question["options"][2])
            optionButton4.config(text=next_question["options"][3])
            amountLabel.config(image=amountImages[i])
            playsound.playsound("next q.wav", block=False)
            time.sleep(1)
        else:
            questionArea.insert(END, "You've completed the quiz!")
    else:
        playsound.playsound("lose.wav", block=False)

def start(e):
    global leftframe, topFrame, centerFrame, bottomFrame, rightframe
    global lifeline50Button, lifelineaudienceButton, lifelineskipButton, logoLabel, amountLabel, layoutLabel, questionArea
    global labelA, optionButton1, labelB, optionButton2, labelC, optionButton3, labelD, optionButton4
    global image50, imageaudience, imageskip, centerImage, layoutImage, questions_data, startbutton
    
    # Destroy the start button after clicking
    

    startbutton.destroy()
    playsound.playsound("amitabh.wav")
    bgimage.destroy()

    leftframe = Frame(root, bg='black', padx=90)
    leftframe.grid(row=0, column=0)

    topFrame = Frame(leftframe, bg='black', pady=15)
    topFrame.grid(row=0, column=0)

    centerFrame = Frame(leftframe, bg='black', pady=15)
    centerFrame.grid(row=1, column=0)

    bottomFrame = Frame(leftframe, bg='black')
    bottomFrame.grid(row=2, column=0)

    rightframe = Frame(root, pady=50, padx=200, bg='black')
    rightframe.grid(row=0, column=1)

    # Add images to lifeline buttons
    image50 = PhotoImage(file='50-50.png')
    lifeline50Button = Button(topFrame, image=image50, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2')
    lifeline50Button.grid(row=0, column=0)

    imageaudience = PhotoImage(file='audiencepole.png')
    lifelineaudienceButton = Button(topFrame, image=imageaudience, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2')
    lifelineaudienceButton.grid(row=0, column=1)

    imageskip = PhotoImage(file='skip.png')
    lifelineskipButton = Button(topFrame, image=imageskip, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2')
    lifelineskipButton.grid(row=0, column=2)

    centerImage = PhotoImage(file='logokbc.png')
    logoLabel = Label(centerFrame, image=centerImage, bg='black', width=300, height=200, bd=0)
    logoLabel.grid(row=0, column=0)

    amountLabel = Label(rightframe, image=amountImages[0], bg='black')
    amountLabel.grid(row=0, column=0)

    layoutImage = PhotoImage(file='layout1.png')
    layoutLabel = Label(bottomFrame, image=layoutImage, bg='black')
    layoutLabel.grid(row=0, column=0)

    questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), width=40, height=2, wrap='word', bg='black', fg='white', bd=0)
    questionArea.place(x=80, y=15)
    questionArea.insert(END, questions_data[0]["question"])

    labelA = Label(bottomFrame, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelA.place(x=60, y=135)
    optionButton1 = Button(bottomFrame, text=questions_data[0]["options"][0], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton1.place(x=100, y=125)

    labelB = Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelB.place(x=400, y=135)
    optionButton2 = Button(bottomFrame, text=questions_data[0]["options"][1], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton2.place(x=435, y=125)

    labelC = Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelC.place(x=60, y=235)
    optionButton3 = Button(bottomFrame, text=questions_data[0]["options"][2], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton3.place(x=100, y=225)

    labelD = Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelD.place(x=400, y=235)
    optionButton4 = Button(bottomFrame, text=questions_data[0]["options"][3], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton4.place(x=430, y=225)

    optionButton1.bind('<Button-1>', select)
    optionButton2.bind('<Button-1>', select)
    optionButton3.bind('<Button-1>', select)
    optionButton4.bind('<Button-1>', select)
    playsound.playsound('q.wav',block=False)

# Create the start button
bgimag = PhotoImage(file='bg.png')
bgimage = Label(root, image=bgimag)
bgimage.place(x=0, y=0)

# Use Pillow to open the play button image

play_photo = PhotoImage(file='play.png')

# Create the play button with transparent image
startbutton = Button(root, image=play_photo, bd=0, bg='black', activebackground='yellow', cursor='hand2')
startbutton.place(x=383, y=405)
startbutton.bind('<Button-1>', start)

root.mainloop()


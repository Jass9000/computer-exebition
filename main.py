from tkinter import *
import playsound
import time
import random


# Initialize i to track the current question, skip flag, and lifeline flag
i = 0
skip_used = False  # Flag to track if skip has been used
lifeline_50_used = False  # Flag to track if 50-50 lifeline has been used
root = Tk()
root.attributes('-fullscreen', True)
root.geometry('1440x900+0+0')
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
    },
    {
        "question": "In a bowl there are six apples. You take away four apples how many do you have?",
        "options": ["4", "2", "6", "3"],
        "answer": "4"
    },
    {
        "question": "Which one of the following salts does not contain water of crystallisation?",
        "options": ["Blue vitriol", "Baking soda", "Washing soda", "Gypsum"],
        "answer": "Baking soda"
    },
    {
        "question": "What is the value of the expression 2^5?",
        "options": ["8", "16", "32", "64"],
        "answer": "32"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the chemical formula for methane?",
        "options": ["CH3", "CH4", "C2H4", "CH2O"],
        "answer": "CH4"
    },
    {
        "question": "Who is the lead actor in the movie 'PK'?",
        "options": ["Shah Rukh Khan", "Aamir Khan", "Salman Khan", "Hrithik Roshan"],
        "answer": "Aamir Khan"
    },
    {
        "question": "Who is the captain of the Indian cricket team as of 2023?",
        "options": ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "Kapil Dev"],
        "answer": "Rohit Sharma"
    },
    {
        "question": "Which Indian cricketer was known for his famous ' Helicopter Shot'?",
        "options": ["Sachin Tendulkar", "MS Dhoni", "Virat Kohli", "Yuvraj Singh"],
        "answer": "MS Dhoni"
    },
    {
        "question": "What is the name of the fictional African country in 'Black Panther'?",
        "options": ["Wakanda", "Zamunda", "Genosha", "Elbonia"],
        "answer": "Wakanda"
    },
    {
        "question": "Which country has the most natural lakes?",
        "options": ["Canada", "Russia", "United States", "India"],
        "answer": "Canada"
    },
     {
        "question": "Who painted the 'Last Supper'?",
        "options": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"],
        "answer": "Leonardo da Vinci"
    },
     {
        "question": "Who Invented The First Smartphone?",
        "options": ["Ronald Wayne", "Steve Jobs", "Frank Canova", "Steve Wozniak"],
        "answer": "Frank Canova"
    },
    {
        "question": "Who Invented The First Laptop?",
        "options": ["Alan Kay", "Adam Osborne", "Charles Babbage", "Sky Li"],
        "answer": "Alan Kay"
    },
]

# Load amount images
amountImages = [PhotoImage(file=f'p{i}.png') for i in range(1, 17)]
prize_money = [
    "₹0","₹1,000", "₹2,000","₹3,000","₹5,000", "₹10,000", "₹20,000", "₹40,000", 
    "₹80,000", "₹1,60,000", "₹3,20,000", "₹6,40,000", "₹12,50,000", 
    "₹25,00,000", "₹50,00,000", "₹1,00,00,000", "₹7,00,00,000"
]

def select(event):
    global i
    a = event.widget
    value = a['text']
    current_question = questions_data[i]

    if value == current_question["answer"]:
        playsound.playsound("clap.wav")
        questionArea.delete(1.0, END)
        i += 1  # Move to the next question
        if i < 16:  # Ensure i doesn't exceed available questions
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
            display_winnings(i)  # If all questions are answered, display final winnings
    else:
        playsound.playsound("lose.wav", block=False)
        
        display_winnings(i)  # Display the amount won before the wrong answer
        
def skip_question():
    global i, skip_used
    if not skip_used and i < len(questions_data) - 1:  # Check if skip hasn't been used and if there is a next question
        playsound.playsound("next q.wav", block=False)
        skip_used = True  # Set the skip flag to True
        i += 1  # Move to the next question
        next_question = questions_data[i]
        questionArea.delete(1.0, END)
        questionArea.insert(END, next_question["question"])
        optionButton1.config(text=next_question["options"][0])
        optionButton2.config(text=next_question["options"][1])
        optionButton3.config(text=next_question["options"][2])
        optionButton4.config(text=next_question["options"][3])
        amountLabel.config(image=amountImages[i])
        imageskip.config(file='skip-used.png')
        lifelineskipButton.config(activebackground='black', bg='black', cursor='')

def lifeline_50_50():
    global lifeline_50_used, i
    if not lifeline_50_used:
        current_question = questions_data[i]
        correct_answer = current_question["answer"]
        options = current_question["options"]
        incorrect_options = [option for option in options if option != correct_answer]

        options_to_remove = random.sample(incorrect_options, 2)

        for option in options_to_remove:
            if option == options[0]:
                optionButton1.config(text="")
            elif option == options[1]:
                optionButton2.config(text="")
            elif option == options[2]:
                optionButton3.config(text="")
            elif option == options[3]:
                optionButton4.config(text="")

        lifeline_50_used = True  # Mark 50-50 lifeline as used
        lifeline50Button.config(activebackground='black', bg='black', cursor='')
        image50.config(file='50-50-used.png')

def display_winnings(index):
    # Stop the game and show the amount won
    for widget in root.winfo_children():
        widget.destroy()
    displaytext=f"Wrong answer correct answer was {questions_data[index]["answer"]}.You won {prize_money[index]}!" if index < 16 else f"You won {prize_money[index]}!" #Shows the right answer if 
    won_label = Label(root, text=displaytext, font=("Arial", 30), bg='cyan', fg='black')
    won_label.pack(expand=True)

    # Delay playing the sound until after the screen has updated
    #playsound.playsound("end.mp3")

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
    lifeline50Button = Button(topFrame, image=image50, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2', command=lifeline_50_50)
    lifeline50Button.grid(row=0, column=0)

    imageaudience = PhotoImage(file='audiencepole.png')
    lifelineaudienceButton = Button(topFrame, image=imageaudience, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2')
    lifelineaudienceButton.grid(row=0, column=1)

    imageskip = PhotoImage(file='skip.png')
    lifelineskipButton = Button(topFrame, image=imageskip, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2', command=skip_question)
    lifelineskipButton.grid(row=0, column=2)

    centerImage = PhotoImage(file='logokbc.png')
    logoLabel = Label(centerFrame, image=centerImage, bg='black', width=300, height=200, bd=0)
    logoLabel.grid(row=0, column=0)

    amountLabel = Label(rightframe, image=amountImages[i], bg='black')
    amountLabel.grid(row=0, column=0)

    layoutImage = PhotoImage(file='layout1.png')
    layoutLabel = Label(bottomFrame, image=layoutImage, bg='black')
    layoutLabel.grid(row=0, column=0)

    questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), width=40, height=2, wrap='word', bg='black', fg='white', bd=0)
    questionArea.place(x=80, y=15)
    questionArea.insert(END, questions_data[i]["question"])

    labelA = Label(bottomFrame, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelA.place(x=60, y=135)
    optionButton1 = Button(bottomFrame, text=questions_data[i]["options"][0], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton1.place(x=100, y=125)

    labelB = Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelB.place(x=400, y=135)
    optionButton2 = Button(bottomFrame, text=questions_data[i]["options"][1], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton2.place(x=430, y=125)

    labelC = Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelC.place(x=60, y=235)
    optionButton3 = Button(bottomFrame, text=questions_data[i]["options"][2], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton3.place(x=100, y=225)

    labelD = Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelD.place(x=400, y=235)
    optionButton4 = Button(bottomFrame, text=questions_data[i]["options"][3], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton4.place(x=430, y=225)

    optionButton1.bind('<Button-1>', select)
    optionButton2.bind('<Button-1>', select)
    optionButton3.bind('<Button-1>', select)
    optionButton4.bind('<Button-1>', select)

    playsound.playsound('q.wav', block=False)

# Create the start button
bgimag = PhotoImage(file='bg.png')
bgimage = Label(root, image=bgimag, bd=0)
bgimage.place(x=-0, y=0)

# Use Pillow to open the play button image
play_photo = PhotoImage(file='play.png')

# Create the play button with transparent image
startbutton = Button(root, image=play_photo, bd=0, bg='black', activebackground='black', cursor='hand2', width=180, height=80)
startbutton.place(x=360, y=111)
startbutton.bind('<Button-1>', start)

root.mainloop()

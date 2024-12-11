from tkinter import *
import playsound
import random
import pyttsx3


def say(a:str, rate:int=200):
    root.update()
    say=pyttsx3.init()
    say.setProperty('rate', rate)
    say.say(a)
    say.runAndWait()


# Initialize i to track the current question, skip flag, and lifeline flag
i = 0
skip_used = False  # Flag to track if skip has been used
lifeline_50_used = False  # Flag to track if 50-50 lifeline has been used
phone_used=False
root = Tk()
root.attributes('-fullscreen', True)

root.title('Kaun Banega Crorepati')
root.config(bg='black')
global questions_data
questions= [
    # Easy
    {
        "question": "What is the capital of the Indian state of Maharashtra?",
        "options": ["Pune", "Mumbai", "Nashik", "Nagpur"],
        "answer": "Mumbai"
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
        "question": "What is the largest ocean on Earth?",
        "options": ["Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
    "question": "What is the unit of force in the SI system?",
    "options": ["Newton", "Pascal", "Joule", "Watt"],
    "answer": "Newton"
    },
    {
        "question": "Who is the lead actor in the movie 'PK'?",
        "options": ["Shah Rukh Khan", "Aamir Khan", "Salman Khan", "Hrithik Roshan"],
        "answer": "Aamir Khan"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Thailand", "Japan", "South Korea"],
        "answer": "Japan"
    },
    {
    "question": "Which state in India is the leading producer of manganese?",
    "options": ["Odisha", "Maharashtra", "Karnataka", "Jharkhand"],
    "answer": "Odisha"
    },

    # Medium
    {
        "question": "The speed of Sound is maximum in which of the following?",
        "options": ["Air at 100°C", "Air at 0°C", "Vaccum", "Same in all"],
        "answer": "Air at 100°C"
    },
    {
    "question": "Which treaty ended the First World War?",
    "options": ["Treaty of Versailles", "Treaty of Vienna", "Treaty of Paris", "Treaty of Westphalia"],
    "answer": "Treaty of Versailles"
    },
    {
        "question": "Which one of the following salts does not contain water of crystallisation?",
        "options": ["Blue vitriol", "Baking soda", "Washing soda", "Gypsum"],
        "answer": "Baking soda"
    },
    {
    "question": "Which acid is commonly used in car batteries?",
    "options": ["Nitric acid", "Sulphuric acid", "Hydrochloric acid", "Acetic acid"],
    "answer": "Sulphuric acid"
    },
    {
    "question": "What is the value of (2x + 3)² when x = 1?",
    "options": ["16", "9", "25", "36"],
    "answer": "25"
    },
    {
        "question": "What is the value of the expression 2^5?",
        "options": ["8", "16", "32", "64"],
        "answer": "32"
    },
    {
        "question": "What is the chemical formula for methane?",
        "options": ["CH3", "CH4", "C2H4", "CH2O"],
        "answer": "CH4"
    },
    {
        "question": "Who is the captain of the Indian cricket team as of 2023?",
        "options": ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "Kapil Dev"],
        "answer": "Rohit Sharma"
    },
    {
        "question": "Which Indian cricketer was known for his famous 'Helicopter Shot'?",
        "options": ["Sachin Tendulkar", "MS Dhoni", "Virat Kohli", "Yuvraj Singh"],
        "answer": "MS Dhoni"
    },
    {
    "question": "Who was the first person to reach the South Pole?",
    "options": ["Robert Scott", "Ernest Shackleton", "Roald Amundsen", "Richard Byrd"],
    "answer": "Roald Amundsen"
    },
    {
        "question": "In which layer of Earth's atmosphere does the ozone layer exist?",
        "options": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
        "answer": "Stratosphere"
    },
    {
    "question": "Who was the first woman to win a Nobel Prize?",
    "options": ["Marie Curie", "Rosalind Franklin", "Indira Gandhi", "Lise Meitner"],
    "answer": "Marie Curie"
    },

    # Hard
    {
        "question": "What is the name of the fictional African country in 'Black Panther'?",
        "options": ["Wakanda", "Zamunda", "Genosha", "Elbonia"],
        "answer": "Wakanda"
    },
    {
    "question": "Which phenomenon explains why the sky appears blue?",
    "options": ["Refraction", "Dispersion", "Scattering", "Diffraction"],
    "answer": "Scattering"
    },
    {
    "question": "Which sector of the Indian economy contributes the largest share to GDP?",
    "options": ["Agriculture", "Industry", "Services", "Manufacturing"],
    "answer": "Services"
    },
    {
    "question": "A ray of light strikes a plane mirror at an angle of 30° with the surface of the mirror. What is the angle of reflection?",
    "options": ["30°", "60°", "90°", "45°"],
    "answer": "60°"
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
    {
        "question": "Which boxer was nicknamed 'The Brown Bomber'?",
        "options": ["Muhammad Ali", "Mike Tyson", "Joe Frazier", "Joe Louis"],
        "answer": "Joe Louis"
    },
    {
        "question": "In statistics, what is the term for the middle value in a set of numbers?",
        "options": ["Mean", "Median", "Mode", "Range"],
        "answer": "Median"
    },
    {
        "question": "Who was the last ruler of the Mughal Empire in India?",
        "options": ["Bahadur Shah II", "Akbar II", "Aurangzeb", "Shah Jahan"],
        "answer": "Bahadur Shah II"
    },
    {
        "question": "What is the speed of light in a vacuum?",
        "options": ["3 x 10^6 m/s", "3 x 10^8 m/s", "3 x 10^10 m/s", "3 x 10^12 m/s"],
        "answer": "3 x 10^8 m/s"
    },
    {
    "question": "Which mathematical constant is approximately 2.71828?",
    "options": ["Pi", "Euler's number", "Golden ratio", "Square root of 2"],
    "answer": "Euler's number"
    },
    {
        "question": "Which acid is known as the king of chemicals?",
        "options": ["Sulfuric Acid", "Nitric Acid", "Hydrochloric Acid", "Acetic Acid"],
        "answer": "Sulfuric Acid"
    }
]


def question_selection():  # Question selection
    global questions_data
    q_ind=sorted( random.sample(range( len(questions) ),16) ) #Generates 16 numbers which 
    questions_data=[questions[i] for i in q_ind]



question_selection()


yellowLayout=[PhotoImage(file=f'y{i}.png') for i in range(1,5)]
redLayout=[PhotoImage(file=f'r{i}.png') for i in range(1, 5)]
greenLayout=[PhotoImage(file=f'g{i}.png') for i in range(1, 5)]
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
    for index in range(0, 4):
        text = current_question["options"][index]
        if value == text:
            break
    changebg(index + 1, "y")
    root.update()
    playsound.playsound("lock.wav")
    if value == current_question["answer"]:
        changebg(index + 1, "g")
        playsound.playsound("clap.wav")

        questionArea.delete(1.0, END)
        i += 1  # Move to the next question
        if i < 16:  # Ensure i doesn't exceed available questions
            next_question = questions_data[i]
            changebg(0,"reset")
            questionArea.insert(END, next_question["question"])
            optionButton1.config(text=next_question["options"][0])
            optionButton2.config(text=next_question["options"][1])
            optionButton3.config(text=next_question["options"][2])
            optionButton4.config(text=next_question["options"][3])
            amountLabel.config(image=amountImages[i])
            playsound.playsound("next q.wav",block=False)
            root.after(2000,lambda: say(f'{next_question["question"]} \n option A . {next_question["options"][0]}\n . option B . {next_question["options"][1]} . option C . {next_question["options"][2]} . option D . {next_question["options"][3]} '))
        else:
            display_winnings(i, False)  # If all questions are answered, display final winnings
    else:
        changebg(index + 1, "r")
        playsound.playsound("lose.wav")
        root.after(1000, lambda: display_winnings(i, True))  # 1-second delay before showing winnings



def phone():
    global i,phone_used
    if not phone_used:
        if 0.3>=random.random():
            wrong_options=[option for option in questions_data[i]["options"] if option != questions_data[i]["answer"]]
            option_by_friend=random.choice(wrong_options)
        else:
            option_by_friend=questions_data[i]["answer"]
        
        imagephoneAFriend.config(file='phoneAFriend-used.png')
        phoneAFriend.config(activebackground='black', bg='black', cursor='')
        root.update()
        playsound.playsound("calling.mp3")
        say(f"Hello everyone,My name is akash, The answer maybe {option_by_friend}",140)
        phone_used=True

def skip_question():
    global i, skip_used
    if not skip_used and i < len(questions_data) - 1:  # Check if skip hasn't been used and if there is a next question
    
        playsound.playsound("next q.wav",block=FALSE)
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
        say(f'{next_question["question"]} \n option A . {next_question["options"][0]}\n . option B . {next_question["options"][1]} . option C . {next_question["options"][2]} . option D . {next_question["options"][3]} ')

def lifeline_50_50():
    global lifeline_50_used, i 
    if not lifeline_50_used:
        current_question = questions_data[i]
        correct_answer = current_question["answer"]
        options = current_question["options"]
        
        incorrect_options = [option for option in options if option != correct_answer]
       
        options_to_remove = random.sample(incorrect_options, 2) # Select

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
        root.update()
        playsound.playsound("after50.mp3")

def display_winnings(index,incorect):
    # Stop the game and show the amount won
    for widget in root.winfo_children():
        widget.destroy()
    if incorect:
        displaytext = f"You selected the wrong answer correct answer was {questions_data[index]['answer']}.\n You won {prize_money[index]}!"  # Shows the right answer if incorrect
    elif index == 16:
        displaytext=f"You won {prize_money[index]}!"
    else:
        displaytext= f"Correct answer was {questions_data[index]['answer']}.\n You won {prize_money[index]}!"
    won_label = Label(root, text=displaytext, font=("Arial", 30), bg='cyan', fg='black')
    won_label.pack(expand=True)
    root.update()
    # Delay playing the sound until after the screen has updated
    playsound.playsound("end.mp3")
def giveup():
    display_winnings(i,False)

def changebg(option_index, state):
    if state == "y":
        optButton[option_index].config(bg="yellow")  # Highlight the selected option
        layoutLabel.config(image=yellowLayout[option_index-1])
        optlabel[option_index].config(bg="yellow")
        root.update()
    elif state == "r":
        optButton[option_index].config(bg="red")  # Highlight the selected option
        layoutLabel.config(image=redLayout[option_index-1])
        optlabel[option_index].config(bg="red")
        root.update()
    elif state == "g":
        optButton[option_index].config(bg="green")  # Highlight the selected option
        layoutLabel.config(image=greenLayout[option_index-1])
        optlabel[option_index].config(bg="green")
        root.update()
    elif state=="reset":
        layoutLabel.config(image=layoutImage)
        for option_index in range(1,5):
            optButton[option_index].config(bg="black")
            optlabel[option_index].config(bg="black")
    root.update()



def start():
    global leftframe, topFrame, centerFrame, bottomFrame, rightframe
    global lifeline50Button, imagephoneAFriend, lifelineskipButton, logoLabel, amountLabel, layoutLabel, questionArea
    global  optionButton1,  optionButton2,  optionButton3, optionButton4
    global image50, phoneAFriend, imageskip, centerImage, layoutImage, questions_data, startbutton
    global imagegiveup,giveupButton
    global optlabel ,optButton
    optlabel = [""]
    optButton=[""]
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

    imagephoneAFriend = PhotoImage(file='phoneAFriend.png')
    phoneAFriend = Button(topFrame, image=imagephoneAFriend, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2',command=phone)
    phoneAFriend.grid(row=0, column=1)

    imageskip = PhotoImage(file='skip.png')
    lifelineskipButton = Button(topFrame, image=imageskip, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2', command=skip_question)
    lifelineskipButton.grid(row=0, column=2)

    imagegiveup=PhotoImage(file="giveup.png")
    giveupButton=Button(topFrame,image=imagegiveup, bg='black', bd=0, activebackground='yellow', width=180, height=80, cursor='hand2', command=giveup)
    giveupButton.grid(row=0,column=3)

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
    optlabel.append(labelA)
    optionButton1 = Button(bottomFrame, text=questions_data[i]["options"][0], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton1.place(x=100, y=125)
    optButton.append(optionButton1)

    labelB = Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelB.place(x=400, y=135)
    optlabel.append(labelB)
    optionButton2 = Button(bottomFrame, text=questions_data[i]["options"][1], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton2.place(x=430, y=125)
    optButton.append(optionButton2)

    labelC = Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelC.place(x=60, y=235)
    optlabel.append(labelC)
    optionButton3 = Button(bottomFrame, text=questions_data[i]["options"][2], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton3.place(x=100, y=225)
    optButton.append(optionButton3)

    labelD = Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
    labelD.place(x=400, y=235)
    optlabel.append(labelD)
    optionButton4 = Button(bottomFrame, text=questions_data[i]["options"][3], bg='black', fg='white', font=('arial', 18, 'bold'), bd=0, activebackground='black', activeforeground='white', cursor='hand2')
    optionButton4.place(x=430, y=225)
    optButton.append(optionButton4)

    optionButton1.bind('<Button-1>', select)
    optionButton2.bind('<Button-1>', select)
    optionButton3.bind('<Button-1>', select)
    optionButton4.bind('<Button-1>', select)
    root.update()
    
    playsound.playsound('next q.wav')
    say(f'{questions_data[i]["question"]} \n option A . {questions_data[i]["options"][0]}\n . option B . {questions_data[i]["options"][1]} . option C . {questions_data[i]["options"][2]} . option D . {questions_data[i]["options"][3]} ')

# Create the baground image
bgimag = PhotoImage(file='bg.png')
bgimage = Label(root, image=bgimag, bd=0)
bgimage.place(x=0, y=0)

# Create the play button 
play_photo = PhotoImage(file='play.png')
startbutton = Button(root, image=play_photo, bd=0, bg='black', activebackground='black', cursor='hand2', width=180, height=80,command=start)
startbutton.place(x=645, y=750)

root.mainloop()

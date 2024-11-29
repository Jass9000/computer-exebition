
import random






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
        "question": "Who is the lead actor in the movie 'PK'?",
        "options": ["Shah Rukh Khan", "Aamir Khan", "Salman Khan", "Hrithik Roshan"],
        "answer": "Aamir Khan"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Thailand", "Japan", "South Korea"],
        "answer": "Japan"
    },

    # Medium
    {
        "question": "The speed of Sound is maximum in which of the following?",
        "options": ["Air at 100°C", "Air at 0°C", "Vaccum", "Same in all"],
        "answer": "Air at 100°C"
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
        "question": "In which layer of Earth's atmosphere does the ozone layer exist?",
        "options": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
        "answer": "Stratosphere"
    },

    # Hard
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
        "question": "Which acid is known as the king of chemicals?",
        "options": ["Sulfuric Acid", "Nitric Acid", "Hydrochloric Acid", "Acetic Acid"],
        "answer": "Sulfuric Acid"
    }
]
def question_selection():  # Question selection
    global questions_data
    q_ind=sorted( random.sample(range( len(questions) ),16) )
    questions_data=[questions[i] for i in q_ind]



question_selection()
for i in range(len(questions_data)):
    print(questions_data[i]["question"])
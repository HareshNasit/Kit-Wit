from FunctionDefinitionsMain import *
from itertools import cycle
import time
#import subprocess
count = 10


Q = ["1. Which sea creature is used as the logo for Waterford Crystal?", \
     "2. Which American singer is the daughter of soul singer Cissy Houston?", \
     "3. Which famous children's book publisher has an insect as its logo?", \
     "4. Which Nintendo video game character can be 'Super' or 'Paper' and sometimes rides a 'Kart'?", \
     "5. What do you do with 'Baked Alaska'?", \
     "6. What do we call a baby goose?", \
     "7. What word completes the following idiom - 'Hop, Skip And ..'?", \
     "8. Which brand of cleaning and polishing products for cars is named after a reptile?", \
     "9. What four living creatures give their names to types of road crossings?", \
     "10. Which British Prime Minister was in power during the Second World War?", \
     "11. What word completes the following idiom - 'Keep It Under Your...'?", \
     "12. Complete the commonly used idiom. 'Their bark is worse than their ...'", \
     "13. AOL are an internet service provider. What does AOL stand for?", \
     "14. In which country are Casablanca and Marrakech?", \
     "15. Which part of Los Angeles has the postal zip code 90210?", \
     "16. What was the name of the world's first National Park?", \
     "17. Why don't cars ever run out of petrol when travelling through the Simplon Tunnel?", \
     "18. In which of the following mythologies was Zeus the King of Gods?", \
     "19. What does OTC stand for, referring to medicines?", \
     "20. What is the name of Halle Berry's character in the 'X Men' movies?", \
     "21. 16th century Spaniards believed there was a region of South America made entirely of gold known by what name?", \
     "22. Which of the following actresses starred in the 1990 film 'Pretty Woman'?", \
     "23. According the the Bible, who did Jesus raise from the dead?", \
     "24. What is the name of Britain's biggest branded bed maunfacturer that shares his name with a Christmas Carol?", \
     "25. Ocimum basilicum is the botanical name for which herb?", \
     "26. Who famously sang 'Happy Birthday' to President Kennedy in 1962"
]
O = [["Frog", "Sea Horse", "Cow", "Tiger"], \
     ["Casey", "Whitney", "Donna", "Britney"], \
     ["Heinemann", "Ladybird", "Harper Collins", "Pearson Longman"], \
     ["Mario", "Luigi", "Pikachu", "Yoshi"], \
     ['Live in it', 'Eat it', 'Drive it', 'Sit on it'], \
     ['Kitten', 'Hatchling', 'Pup', 'Gosling'], \
     ['Fall', 'Jump', 'Leap', 'Charge'], \
     ['Collinite', 'Dodo Juice', 'Turtle Wax', 'Valet Pro'], \
     ['Puma, donkey, parrot, puffin', 'Camel, bear, lizard, seagull', 'Ostrich, horse, turtle, snail', 'Zebra, pelican, puffin, toucan'], \
     ['Margaret Thatcher', 'Gordon Brown', 'Tony Blair', 'Sir Winston Churchill'], \
     ['Bat', 'Cat', 'Mat', 'Hat'], \
     ['Roots', 'Casserole', 'Bite', 'Leaves'], \
     ['America Online', 'Asia Online', 'Australia Online', 'Africa Online'], \
     ['Algeria', 'Liberia', 'Morocco', 'Senegal'], \
     ['Pasadena', 'Norwalk', 'Long Beach', 'Beverly Hills'], \
     ['Chobe National Park', 'Yellowstone National Park', 'Bukhansan National Park', 'Tlemcen National Park'], \
     ['It\'s a motorway', 'It\'s a railway tunnel', 'It\'s a lane', 'It\s a road'], \
     ['Egyptian', 'Norse', 'Greek', 'Roman'], \
     ['Over the counter', 'Officer Trading Corps', 'Offshore Technology Conference', 'Oriental Trading Company'], \
     ['Sun', 'Rain', 'Storm', 'Wheat'], \
     ['El Hamfrabo', 'El Geralo', 'El Borano', 'El Dorado'], \
     ['Julia Roberts', 'Cameron Diaz', 'Penelope Cruz', 'Reese Witherspoon'], \
     ['Clopas', 'Nicodemus', 'Cleopas', 'Lazarus'], \
     ['Sweetdreams', 'Cbbeds', 'Silentnight', 'Bedfed'], \
     ['Thyme', 'Dill', 'Basil', 'Chives'], \
     ['Doris Day', 'Audrey Hepburn', 'Marilyn Monroe', 'Elizabeth Taylor'], \
    ] 
A = ["Sea Horse", "Whitney", 'Ladybird', 'Mario', 'Eat it', 'Hatchling', \
     'Jump', 'Turtle Wax', 'Puma, donkey, parrot, puffin', 'Tony Blair', \
     'Hat', 'Bite', 'Africa Online', 'Senegal', 'Norwalk', 'Yellowstone National Park', \
     'It\'s a lane', 'Roman', 'Officer Trading Corps', 'Wheat', 'El Dorado', \
     'Reese Witherspoon', 'Lazarus', 'Silentnight', 'Chives', 'Elizabeth Taylor']
Opts = ['A. ', 'B. ', 'C. ', 'D. ']
OptLabelDict = {}

#Ques_Opt = [(question, qopts) for question, qopts in Questions, Options]
#print Ques_Opt
No_of_ques = 25
Q_O_A = []
CountDownval = tk.StringVar(root, '10')
skipclear = 1

for i in range(No_of_ques):
    Q_O_A.append((Q[i], O[i], A[i]))
Ques_Opt_Ans = cycle(Q_O_A)

def CheckAnswer(Chosen, Actual, answerindex):
    global R_W, scoreval
    flag = 0
    for value in OptLabelDict.values():
        textval = value.cget("text")
        for Opt in Opts:
            textval = textval.lstrip(Opt)
        if textval == Actual:
            value.configure(bg = 'green')#to get attribute value
        else:
            value.configure(bg = 'red')

    #if Chosen == Actual:
    R_W = tk.Label(new.main, text = 'Correct', font = ('times', 25, 'bold'), bg = 'black', fg = 'white')
    R_W.grid(column = 0, columnspan = 2, row = 3)
    if Chosen != Actual:
        R_W.configure(text = 'Wrong')
        flag = 1
    if flag == 0:
        currscore = scoreval.get().split(' ')
        currscore[1] = str(int(currscore[1]) + 1)
        newscore = ' '.join(currscore)
        scoreval.set(str(newscore))

    root.after(100, QuestionWindow)

def CountUpdate():
    global count
    while count > 0:
        print CountDownval.get()
        NewCount = str(int(CountDownval.get()) - 1)
        CountDownval.set(NewCount)
        count -= 1
        root.after(1000, CountUpdate)
    return

def Restart():
    for child in new.main.winfo_children():
        child.destroy()
    #del endprog
    creation()
    

def EndScreen():
    global skipclear, CountDownval
    if skipclear == 1:
        for child in new.main.winfo_children():
            child.destroy()
        skipclear = 0
    Score = int((scoreval.get().split("Score: "))[1])
    if Score > 20:        
        tk.Label(new.main, text = "Proceed to the nearest deputy for further information.")
    if Score < 20:
        #print 'running fail'
        new.main.grid_configure(padx = (0, 0))
        tk.Label(new.main, text = "You have failed to acquire the required minimum score.", font = ('times', 50, 'bold'), fg = 'white', bg = 'black').grid(column = 0, row = 0, pady = (70, 70))
        #CountDown = tk.Label(root, textvariable = CountDownval, font = ('times', 50, 'bold'), fg = 'white', bg = 'black')
        #CountDown.grid(column = 0, row = 1)
        tk.Label(new.main, text = "Please exit and restart.", font = ('times', 50, 'bold'), fg = 'white', bg = 'black').grid(column = 0, row = 1, pady = (70, 70))
        root.columnconfigure(0, weight = 1)
        root.rowconfigure(0, weight = 1)
        root.rowconfigure(1, weight = 1)
        #CountUpdate()
        #root.after(1000, Restart)       
        return
    

def QuestionWindow():
    global endprog
    try:
        R_W.destroy()
    except NameError:
        pass
    for value in OptLabelDict.values():
        value.configure(bg = 'black')
    Question, Options, Answer = next(Ques_Opt_Ans)
    if Q.index(Question) == 0:
        try:
            if endprog == 1:
                del endprog
                EndScreen()
                return
        except NameError:
            endprog = 1
        
    print Question
    QuesL.configure(text = Question)
    if len(Question)*15 < 1100:
        new.main.grid_configure(padx = (int((new.width-len(Question*15))/2.0), 0))
        print ((new.width-len(Question*15))/2.0), len(Question)
    else:
        new.main.grid_configure(padx = (int((new.width-1100)/2.0), 0))
    print (new.width - len(Question))/2.0, 'identify'
    index = 0
    answerindex = Options.index(Answer)
    for value in OptLabelDict.values():
        value.configure(text = Opts[index] + Options[index], command = lambda Optionsval=Options[index]: CheckAnswer(Optionsval, Answer, answerindex))
        index+=1

def creation():
    global QuesL, OptL, OptLabelDict, Score, scoreval
    QuesL = tk.Label(new.main, text = '', font = ('times', 30, 'bold'), fg = 'red', bg = 'black', wraplength = 1100)
    QuesL.grid(column = 0, columnspan = 2, row = 0, pady = (0, 50))

    rowval = 1
    column = 0
                                                                                
    for i in range(4):
        if i>=2:
            if rowval == 1:
                rowval += 1
            else:
                pass
                                                                               
        OptL = tk.Button(new.main, text = Opts[i], bg = 'black', fg = 'white', font = ('times', 20, 'bold'), width = 30)
        OptL.grid(column = column, row = rowval, pady = (0, 50), padx = (0, 60))
        if column == 0:
            column = 1
        elif column == 1:
            column = 0

        OptLabelDict["Opt"+str(i)] = OptL

    scoreval = tk.StringVar(new.main, 'Score: 0')
    Score = tk.Label(new.main, textvariable = scoreval, bg = 'black', fg = 'white', font = ('times', 20, 'bold'))
    Score.grid(column = 0, columnspan = 2, row = 4)
    QuestionWindow()


creation()
root.mainloop()

#Create a Random Password Generator in Python

from random import choice

def question():
    Input = input("Restart y/n ?")
    
    if Input == "y":
        Rand()
    elif Input == "n":
        exit()
    else:
        question()

def Rand():
    Input_ = input("Enter the number of digits: ")
    def creat_Rand(I):
        pas = ""
        dictionary = "123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#$_&-+/*.,~`="
        try:
            Input = int(Input_)
            for i in range(Input):
                pas += choice(dictionary)
        except:
            Rand()
        return pas
    print(creat_Rand(Input_))
    question()
Rand()

import random 

com = random.randint(1,100)
while True:
    num1 = int(input("Guess the Number between 1 to 100 :-"))

    if num1 == com:
        print(" hurrah !! you won the game!")
        break
    elif num1>com:
         print("sorry wrong guess go lower!")
    elif num1<com:
        print("sorry wrong guess go higher!") 
#imports
import random
import time

# comments!!!! where you would want to take notes

'''
multiline comments
I'm still in a comment!!!
'''

#loosely typed - python figures out what type you are trying to assign
Welcome_message = "The 💣 will explode in 3 incorrect guesses. Will you survive?"
min_number = 1
max_number = 10
secret_number = random.randint(min_number, max_number)
is_correct = False

print(Welcome_message)
print(f"The correct number is between {min_number} and {max_number}")
print(f"You have three attempt. Good luck bwahahah! \"huehuehue!\" 😈")

# always use (==) to compare two things always use (=) to assign a value
#first guess
guess = int(input("Go ahead and enter your first guess: "))
if guess == secret_number:
    print("You guessed it on your first try 😈 Enjoy your freedom... ")
    is_correct = True
elif guess < secret_number:
    print("You guessed Too low 😈 Try again! ")
    print() #empty line
else:
    print("Too high 😈 Try again! ")
    print() #empty line

#second guess
if not is_correct:
    guess = int(input("You're getting closer to your demise, Enter your 2nd guess: "))
    if guess == secret_number:
        print("Curses your 2nd guess was correct! 😈 Enjoy your freedom... ")
        is_correct = True
    elif guess < secret_number:
        print("You guessed Too low 😈 Try again! ")
        print() #empty line
    else:
        print("Too high 😈 Try again! ")
        print() #empty line
        



#3rd guess
if not is_correct:
    guess = int(input("Last chance to get your freedom 😈 Enter your final guess: "))
    
    if guess == secret_number:
        print("How did you...? 😈 You have survived for now... ")
        is_correct = True
    else:
        print("Incorrect! The number was: ", secret_number)
        print("😈 Your time has come bwahaha!")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("💥💥💥💥💥💥💥")
        time.sleep(1)
        print()

    if it is correct:
        print("You have survived for now... ")
         

   

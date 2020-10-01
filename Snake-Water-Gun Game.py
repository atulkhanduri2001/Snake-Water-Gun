import random

lst = ['s', 'w', 'g']
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)


if __name__ == '__main__':
    speak("Welcome...please enter your name")
    hh = input("please enter your name:")
    speak("You will be given 10 chances .......Please select snake ,,water,, or gun")
print(" \t \t \t \t SNAKE, WATER, GUN  Game\n \n")
print("'s' for snake \n 'w' for water \n 'g' for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        # speak("sanke...water...gun")
        print("Tie Both 0 point to each \n ")
        speak("Its a tie")
        speak(f"your point {human_point}and computer's point {computer_point}....")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        # speak("snake..water,..gun..game.")
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
        speak(f"Your point {human_point} ,computers point{computer_point}....")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        # speak(" snake,..water,..gun..game.")
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")
        speak(f"Your point {human_point} ,computers point{computer_point}....")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        # speak(" snake,..water,..gun..game.")
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
        speak(f"Your point {human_point} ,computers point{computer_point}....")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        # speak(" snake,..water,..gun..game.")
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")
        speak(f"Your point {human_point} ,computers point{computer_point}....")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        # speak(" snake,..water,..gun..game.")
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")
        speak(f"Your point {human_point} ,computers point{computer_point}....")



    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        # speak(" snake,..water,..gun..game.")
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
        speak(f"Your point {human_point} ,computers point{computer_point}....")

    else:
        speak("You have entered wrong input")
        print("you have input wrong \n")
        speak("Wrong input....")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
    speak("please play your next turn")

print("Game over")

if computer_point == human_point:
    speak("its a tie match... well played")
    print("Tie")

elif computer_point > human_point:
    speak("computer won the match")
    print("Computer wins and you loose")

else:
    speak(f"Congratulation {hh} you won the match")
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

speak(f"your point {human_point} and computer {computer_point}")

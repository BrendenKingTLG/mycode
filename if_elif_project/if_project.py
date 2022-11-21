# Brenden King
# 11-17-2022
# this program determines if a person should become a swe

# imports
import os
import time

#play again 
def play_again():
    user_input = input("\nif you would like to try again enter yes\n").upper()
    if user_input == "YES":
        main()
    else:
        print("Thanks for playing!")


# determination
def determination(points_scored):
    print("now that you have answered all the questions lets find out what you scored")
    clear()
    print("your result is: ")
    if points_scored >= 40:
        print("you should seriously consider becoming a software engineer")
    elif points_scored >= 30:
        print("you might want to try out software engineering")
    else:
        print("you do not have what it takes to be a software engineer ... sorry")


# clear screen
def clear():
    os.system('clear')


# questions and point addition
def questions():
    question_list = [
            "I like working with people.",
            "I have a knack for problem solving.",
            "I like to listen to music.",
            "I like to find patterns in things.",
            "I like learning/trying new things.",
            "I am intrinsically motivated.",
            "I love technology.",
            "I can see myself as a software developer.",
            "I consider myself a masochist.",
            "Would you consider yourself a strong communicator."
            ]
    points_scored = 0
    for question in question_list:
        print(f"{question} \n\nhow much do you agree with the statement above?\n")
        while True:
            user_input = input("\t 5 - strongly agree \n \t 4 - agree \n \t 3 - neutral \n \t 2 - disagree \n \t 1 - "
                               "strongly disagree \n")
            if user_input == "5":
                points_scored += 5
                break
            elif user_input == "4":
                points_scored += 4
                break
            elif user_input == "3":
                points_scored += 3
                break
            elif user_input == "2":
                points_scored += 2
                break
            elif user_input == "1":
                points_scored += 1
                break
            else:
                clear()
                print("I told you to pick a damn number....lets try again\n")
                print(f"{question} \n\nhow much do you agree with the statement above?\n")
        q_break()
    return points_scored


#break in between questions
def q_break():
        clear()
        print("thank you for answering.. lets move on")
        time.sleep(2)
        clear()


#introduction
def intro():
    clear()
    print("hello friend, I heard you were thinking about becoming a software engineer?")
    time.sleep(4)
    clear()
    print("take this short quiz to determine if software engineering is right for you")
    time.sleep(4)
    clear()


# main
def main():
    intro()
    points = questions()
    determination(points)
    play_again()


main()


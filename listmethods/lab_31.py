#!/usr/bin/python3
import random

wordbank= ["indentation", "spaces"]

tlgstudents= []

wordbank.append(4)

passcode = 1234

with open("names.txt") as file:
    for line in file:
        tlgstudents.append(line.rstrip())


def student_search():
    student_count = len(tlgstudents)
    student_number = input(f"Please enter the students number (between 1 and {student_count}) or enter random for a random student: ")
    if (student_number.lower() == "random"):
        student_name = tlgstudents[random.randint(1, student_count)]
    elif (int(student_number) in range(0, student_count + 1)):
        student_number = int(student_number) - 1
        student_name = tlgstudents[student_number]
    else:
        print("please enter a valid input")
    print(f"{student_name} always uses {wordbank[-1]} {wordbank[-2]} to indent.")


def student_add():
    auth = int(input("please enter passcode to add student: "))
    if (auth == passcode):
        new_student = input("Please enter the first name of the new student: ")
        with open("names.txt", "a") as file:
            file.write(f"{new_student}\n")
        print("operation complete")
    else:
        print("incorrect authentication, operation dismissed")


def menu():
    while True:
        action = int(input("hi, what would you like to do: 1-search 2-add 3-quit: "))
        if (action == 1):
            student_search()
        elif (action == 2):
            student_add()
        elif (action == 3):
            break
        else:
            print("input not valid, operation dismissed")

menu()

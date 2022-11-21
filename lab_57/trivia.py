#!/usr/bin/env python3
import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }


category = trivia["category"]
q_type = trivia["type"]
question = trivia["question"]
correct_answer = html.unescape(trivia["correct_answer"])
incorrect_1 = html.unescape(trivia["incorrect_answers"][0]) 
incorrect_2 = html.unescape(trivia["incorrect_answers"][1]) 
incorrect_3 = html.unescape(trivia["incorrect_answers"][2])

print("hi welcome to the game, please answer the folling question")
print(f"keep in mind your catagory is {category} and your question type is {q_type}")
print(f"your question is: {question}\n")
ans = input(f"please select from the following choices: \n a - {correct_answer} \n b - {incorrect_1} \n c - {incorrect_2} \n d - {incorrect_3}\n")
if(ans == "a"):
    print("yay you got the question right")
else:
    print(f"sorry you got the question wrong, your trash...dont ever play this game again. The correct answer was option 1: {correct_answer}")

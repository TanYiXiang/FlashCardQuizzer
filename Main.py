import random
import time
import sys
import os

EXIT_COMMAND = 'exit'

# Obtain quiz questions file path from user.
while True:
    questionFilePath = input('Input flashcards file path: ')
    if os.path.exists(questionFilePath):
        break
    else:
        print('Invalid file path provided, please try again.')

# Assemble the questions from the text file.
questionFile = open(questionFilePath)
answerDict = {}
questionList = questionFile.readlines()
for question in questionList:
    dictComp = question.split(",")
    questions = dictComp[0]
    answerKey = dictComp[1].rstrip('\n')
    answerDict[questions] = answerKey

# Randomly select question from question list and prompt for answer.
while True:
    question = random.choice(list(answerDict.keys()))
    print(question + '?')
    answer = input()
    if answer.lower() == answerDict[question].lower():
        print('Correct! Nice job.')
    elif answer.lower() == EXIT_COMMAND:
        break
    else:
        print('Incorrect')

# Exit the quiz
print('Goodbye!!')
time.sleep(2)
sys.exit()

# FlashCard Quizzer

A Python script that takes a file containing flash card questions and answers as an argument 
and quizzes the user based on the contents of that file until the user quits the program.
The flash card file should be in the form:
```	
	question,answer
	question,answer
	question,answer
	question,answer
	...
```

## Instructions

Step 1) Provide flash card file path when prompted

Step 2) A random question will be selected and shown. Type in the answer in the next line.

Step 3) Answer will be compared and feedback provided.

Step 4) 2-3 will be repeated until 'exit' is typed.

## Example usage
```
Input flashcards file path: D:\Python Projects\State Capital FlashCard Quiz\state_capitals.txt
Texas? 
Austin
Correct! Nice job.
New Mexico? 
Santa Fe
Correct! Nice job.
Oregon? 
Portland
Incorrect. 
Virginia? 
Exit
Goodbye!!
```

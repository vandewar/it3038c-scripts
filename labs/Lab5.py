import random

luckyNum = random.randrange(0, 20, 1)

print('Guess a number between 0 and 20')

while True:
	guessNum = int(input())
	if guessNum > luckyNum:
		print('Try guessing something lower')
	elif guessNum < luckyNum:
		print('Try guessing something higher')
	else:
		print('Nice guess, you got it!')
		break
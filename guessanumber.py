import random

def guessing_game():
	number = random.randint(0, 100)
	tries = 7
	print("I'm thinking of a number between 0 and 100.")
	while tries > 0:
		print("You have {} guesses remaining.".format(tries))
		guess = int(input("enter your guess: "))
		tries -= 1
		if guess == number:
			break
		elif guess > number:
			print("Too High.")
		else:
			print("Too Low.")
		
	if guess == number:
		print("Well done! You guessed the number {} in {} tries.".format(number, 7 - tries))
	else:
		print("Thank you for playing--but you didn't guess the number. It was: {}".format(number))

if __name__ == "__main__":
	guessing_game()

import random

#### FUNCTIONS ####
'''
Randomly selects a secret word from a bank of over 50,000 words. Returns the secret word.
'''
def pick_word():
	wordbank = open("word_bank.txt","r") #opens text file for reading
	words = wordbank.read() #stores contents of txt file in variable
	words = words.split() #place words into a list.
	return random.choice(words)

'''
Takes in the number of incorrect guesses as an argument and prints the approptiate hangman status.
'''
def print_body(num):
	if num ==0:
		print("_______")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
	elif num == 1:
		print("_______")
		print("|     0")
		print("|")
		print("|")
		print("|")
		print("|")
	elif num ==2:
		print("_______")
		print("|     0")
		print("|     |")
		print("|")
		print("|")
		print("|")
	elif num ==3:
		print("_______")
		print("|     0")
		print("|    /|")
		print("|")
		print("|")
		print("|")
	elif num ==4:
		print("_______")
		print("|     0")
		print("|    /|\\")
		print("|")
		print("|")
		print("|")
	elif num ==5:
		print("_______")
		print("|     0")
		print("|    /|\\")
		print("|    / ")
		print("|")
		print("|")
	elif num ==6:
		print("_______")
		print("|     0")
		print("|    /|\\")
		print("|    / \\")
		print("|")
		print("|")








		
#### GAME #####
# Select secret word
secret_word = pick_word()

# Create dashes list

# Create list of previous guess

#Create a variable that store the number of incorrect guesses


##### GAME LOOP #### 
# while loop that runs as long as the number of incorrect guess is less than 6 and there are "_" in the dashes list


	# Display gallows

	# Display dashes

	# Ask player for guess and process guess

# Print a message - If the player wins, write a congratualtory message, otherwise let the know they lost and print the secret word.




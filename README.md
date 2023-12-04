# Hangman 
Hangman is a popular word game in which one player (the "chooser") chooses a secret word and another  player (the "guesser") attempts to guess the word one letter at a time. If a guessed letter appears in the word,  all instances of it are revealed. If not, the guesser loses a chance. If the guesser figures out the secret word  before he or she runs out of chances, he or she wins. If not, the player who chose the word wins. Traditionally,  chances are tracked using a stick figure drawing of a person being hanged from a gallows. The figure is drawn  one body part at a time, and the guesser loses when the entire figure has been drawn.

## Details 
### Behavior 
**Gameplay** 

In our implementation of Hangman, the computer will take on the role of the "chooser" and the  human player will be the "guesser." The computer will secretly choose a word from a list (see  below) and show the player how many letters are in the word by displaying a sequence of  blanks (underscores). Then, the computer will begin asking for guesses. If the player guesses a  letter that is in the secret word, all blanks representing an instance of that letter should be  replaced by the letter. If the guessed letter is not in the word at all, the player should lose a  chance and a new part of the Hangman figure should appear. If the player guesses a letter he or  she has already guessed, he or she should not lose a chance, even if that letter is not in the  word. If the player guesses all letters in the word, he or she wins. If the Hangman figure is  completed, the player loses. In either case, the secret word should be revealed after the game  is over.

**Word Status:** 

As the game is played, the player should be shown the current guessed status of the secret word. Letters that have been correctly guessed should be shown in the correct locations.  Unguessed letters will appear as blanks. At the beginning of the game, no letters will have been  guessed, and the only information shown to the player will be a sequence of blanks, with one  blank for each letter in the secret word. As the player guesses letters correctly, blanks representing guessed letters should be replaced by those letters. So, for example, if the secret  word is "screwdriver" and the player has guessed 'e,' 's', 'r', and 'd,' the current word status  would be "s r e d r e r". 

**Chances/The Hangman:** 

The player will have six "chances" to guess the word. Guessing a correct letter does not cost a  chance. Each missed chance will cause a new piece of the Hangman to appear. The six pieces of  the Hangman are: head, body, left arm, right arm, left leg, right leg. 

**Game End:** 

The game can end in one of two ways: 
- If the player has guessed the complete secret word, he or she wins. 
- Otherwise, if the player has run out of chances and the complete Hangman has been drawn, the player loses.

In either case, when the game ends the host should stop asking for guesses. The host should  inform the player whether he or she won or lost, and the assistant should reveal the entire  secret word.



### Functions 
**Provided Functions:**
- *pick_word()* - randomly selects and returns a word from a word bank with 58110 words
- *print_body(incorrect)* - Takes in the number of incorrect guesses and displays the gallows and the correct body parts

<br></br>
**Functions to be written:**
### starting_dashes(secret_words)

Takes in the secret word as an argument. It returns a list which contains an underscore for every letter in the secret word.  
- This function is called once.
- Hint: use a for loop to iterate across the secret word

***Function call:***
```python
secret_word = "moon"
dashes = starting_dashes(secret_word)
print(dashes)
```
***Output***
```python
["_","_","_","_"]
```
<br></br>
### display_dashes(dashes)
Print the "_" and letters in the list of dashes
Options:
1. a for loop that iterates across the secret word
2. print(" ".join(dashes))

***Function call:***
```python
secret_word = "moon"
dashes = starting_dashes(secret_word)
display_dashes(dashes)
```
***Output:***
```python
_ _ _ _
```

<br></br>
### replace_dashes(dashes, secret_word, guess)

Takes in the list of dashes, the secret_word and the player's guess as arguments. The function replaces all the "_"s at the indexes where the guess appears in the secret word. The list of dashes is returned.
- Use a for loop with the range() function. The range function produces index values that can be use to iterate across the secret word and can be used to indicate which "_" needs to be replaced.

***Function call:***
```python
dashes = replace_dashes(["_","_","_","_"], "moon", "o")
display_dashes(dashes)
```
***Output:***
```python
_ o o _
```

<br></br>
### check_guess(dashes,secret_word, guess, previously_guessed, num_incorrect)
Check to see if the guess is the secret word or if the guess is a letter in the secret word. It will make the appropriate changes to the list of dashes if the letter is found in the secret word or it will increment the number of incorrect guess if the guess is not in the word.
1. Determines if the player has made the same guess previously. If the player has previously made the guess, an error message should be print and return the the list of dashes, the list of previous guesses and the number of incorrect should be returned. Otherwise, it should preceed to Step 2.
2. Add the guess to the list of previous guesses.
3. Determine if the player's guess is letter or a guess. If the guess is a word, check to see if the guess matches the secret word. If it is print a celebratory message and replace every "_" in the list of dashes with the correct letter. Return the the list of dashes, the list of previous guesses and the number of incorrect should be returned. Otherwise proceed to Step 4.
4. Check to see if the guess is in the secret word. If it is not print an error message, add one to number of incorrect guesses and return the the list of dashes, the list of previous guesses and the number of incorrect should be returned. If guess is in the wecret word, call on the replace_dashes() function and return the the list of dashes, the list of previous guesses and the number of incorrect should be returned.

***Function call:***
```python
dashes, previously_guessed, num_incorrect = check_guess(["_","_","_","_"], "moon", "o",["e","a"],2)

display_dashes(dashes)
print("List of previously guessed letters:",previously_guessed)
print("The number of incorrect guesses:",num_incorrect)
```
***Output***
```python
_ o o _
List of previously guessed letters: ["e","a","o"]
The number of incorrect guesses: 2
```
---
***Function call:***
```python
dashes, previously_guessed, num_incorrect = check_guess(["_","_","_","_"], "moon", "i",["e","a"],2)

display_dashes(dashes)
print("List of previously guessed letters:",previously_guessed)
print("The number of incorrect guesses:",num_incorrect)
```
***Output***
```python
_ _ _ _
List of previously guessed letters: ["e","a","i"]
The number of incorrect guesses: 3
```
---
***Function call:***
```python
dashes, previously_guessed, num_incorrect = check_guess(["_","_","_","_"], "moon", "moon",["e","a"],2)

display_dashes(dashes)
print("List of previously guessed letters:",previously_guessed)
print("The number of incorrect guesses:",num_incorrect)
```
***Output***
```python
m o o n
List of previously guessed letters: ["e","a","moon"]
The number of incorrect guesses: 2
```


---
## RUBRIC
|Description|Points|
|---|---|
|Program selects a random word from the text file to be the secret word.|1 pt. |
|Program displays one "_" for each letter in the word at the beginning of the game.| 1 pt.|
|Program repeatedly prompts the player for a guess until the player has correctly guessed the word or has run out of guesses.| 1 pt. |
|If the player guesses a letter that is in the secret word, all blanks representing an instance of that letter should be replaced by the letter| 2 pts.|
|If the guessed letter is not in the word at all, the player should lose a chance and a new part of the Hangman figure should appear. | 2 pts.|
|If the player guesses a letter he or she has already guessed, he or she should not lose a chance, even if that letter is not in the word.|2 pts.|
|If the player guesses the secret word, all blanks should be replaced with the correct letters| 2 pts.|
|As the game is played, the player should be shown the current guessed status of the secret word. Letters that have been correctly guessed should be shown in the correct locations. Unguessed letters will appear as blanks.|2 pts.|
|If the player guesses all letters in the word, he or she wins. The program should print a celebratory message which includes the secret word.| 2 pts.|
|If the Hangman figure is completed, the player loses, and the program should print a message informing the player of the secret word.|2 pts.|
|Each missed chance will cause a new piece of the Hangman to appear. The entire body should be displayed when the player loses.| 1 pt.|
|**TOTAL:** |18 pts.|
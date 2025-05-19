#import random module for random selection of list items 
import random

#set intial number of lives to 10
lives=10

#create a list with possible words to be randomly selected
#ensure all words are exactly five characters
words=['hello', 'otter', 'games', 'enemy', 'weird', 'lemon']

#store randomly selected secret word in separate variable
secret_word=random.choice(words)

#store question marks as a list in the clue variable
clue=list('?????')

#store heart character in variable to make code cleaner later on
heart=u'\u2764'

#use Boolean to set intial guess to false
correct_guess=False

#Welcome message and instructions
print('\n Welcome to the word guessing game! \n\n To win the game, you must correctly guess the secret word, hidden behind the question marks. Each correct guess will reveal the position of the letter. When you think you have the whole word, submit your guess. \n But be warned, for every wrong guess, you will lose one of your precious lives. You will begin with ten lives. \n\n Best of luck, and enjoy! ')

#function checks through each letter in the secret word and if it matches the guess, then the question mark at that position is replaced with the letter
def update_clue(guessed_letter, secret_word, clue):
    #starting from the first letter
    index=0
    #will only loop while the index position is shorter than the length of the word 
    while index<len(secret_word):
        #if guessed letter is equal to the letter at current position in secret word....
        if guessed_letter == secret_word[index]:
            #...then the question mark at that position is replaced with the letter
            clue[index]=guessed_letter
        #moves to next index position 
        index=index+1

#while there are still lives remaining    
while lives>0:
    #print the clue list and number of lives left. 
    print(clue)
    #number of lives must be converted to string before concatenation
    print('Lives left: ' + heart*lives + '   ' + str(lives))
    #stores input from user's guess in variable
    guess=input('Guess a letter or the whole word: ')

    #if the input is exactly equal to original secret word then the guess Boolean changes to tru and the loop is broken
    if guess == secret_word:
        correct_guess = True 
        break

    #if the letter guessed is contained within the secret word, then message is displayed and clue list is updated with the letter
    if guess in secret_word:
        print('Nice work. The letter ' + guess + ' is in the word. \n')
        #clue list updated with three parameters taken as arguments
        update_clue(guess, secret_word, clue)
    else:
        #print error message if letter is not in secret word
        print('Incorrect. You lose a life \n')
        #remove a life
        lives=lives-1

#if the while word is guessed correctly, correct_guess will become True and message displayed accordingly
if correct_guess:
    print('You did it! The secret word was: '+ secret_word)
#if not, failure message appears and game is over
else:
    print('Not quite. The secret word was: '+ secret_word)


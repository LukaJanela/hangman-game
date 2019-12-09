from random import randint

#Hangman Game

#all the words available are stored in this list
word_list = []
#this list is used to store above words but without newline characters (rstrip method)
new_word_list = []

#opens file with the list of words in it
with open('hangman_words.txt') as file_obj:
    word_list = file_obj.readlines()

#save words without newline character in new list(subject to change)
for word in word_list:
     new_word_list.append(word.rstrip('\n'))


#choosing a word from above list with randint
secret_word = new_word_list[randint(0, len(word_list))]
#initializing amount of dashes for a secret word
dashes = '-'*(len(secret_word))
#number of guesses user has (10 in this case)
guesses_left = 10

#loop ends if secret word and user guesses word(after filling all dashes) are equal
#and he has positive number of guesses left
while secret_word != dashes and guesses_left >= 0:
    #first print dashes
    print (dashes)
    #then take user input
    user_input = input('Enter a letter: ')
    #print how many guesses user has left
    print ('You have ' + str(guesses_left) + ' guesses left\n')

    #if the guess is correct
    if user_input in secret_word:
        #print this message
        print ('That letter is in a word!')
        #and change dashes string with new string, which countains letter user just guesses
        dashes = change_dashes(secret_word, user_input, dashes)
    else:
        #if they didn't guess, decrement user's guesses by 1
        guesses_left -= 1
        
#changes dashes string with a new string which contains guessed letters
def change_dashes(secret_word, user_letter, current_word):
    #initiate empty string which will be returned at the end
    result = ''
    
    #iterate over dashed string
    for i in range(len(current_word)):
        #if user's letter is in secret word
        if user_letter == secret_word[i]:
            #append this letter to result string
            result += user_letter
        else:
            #if not, add characters which are in dashed string
            #this includes dashes and letters which user had already guesses
            result += current_word[i]
    
    return result
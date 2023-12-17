import random 

def dict(file_path): 
    with open(file_path) as f:
        words = [line.strip() for line in f]
        return words 
    
def isValid(guess, guesses):
    return guess in guesses

def checks(guess , word):
    str= ""

    for i in range(5):
        if guess[i] == word[i]:
            str+= '🟩'
        else: 
            if guess[i] in word:
                str+='🟨'
            else:
                str+= '⬛'  
    return str 

def wordle (guess, words):
    print("welcome to wordle get 6 chances to guess a 5 letters word")
    secretWord = random.choice(words)

    attemps= 1
    maxatt= 6

    while attemps <= maxatt:
        guess = input("enter your guesse #" + str(attemps) + " : ").lower()
        if not isValid(guess, guesses):
            print("invalid guess, please try againg")
            continue
        if guess == secretWord:
            print (" yay!! you guessed it right! in ",str(attemps) + " trys" )
            break
        attemps +=1
        feedback = checks(guess, secretWord)
        print(feedback)

    if attemps > maxatt: 
       print ( " game over , the secret word was ", secretWord)

guesses = dict("words.txt")
words = dict("answer.txt")

wordle(guesses, words)

from random import choice

# Initial setup
tries = 8
repeat = 0
repeat_allowed = 6

# Parameters for display purpose
word = choice("initial display purpose interesting calories chocolate classic birthday popular \
               sandwich chicken people broccoli popeyes manager manhattan columbus circle \
               computer history student assisstant youtube california potato opponent customer \
               mushroom window romance sherlock ".split())
word_dict = dict()
out = ["_"] * len(word)
guessed = set()

for index, char in enumerate(word):
    if not word_dict.get(char):
        word_dict[char] = [index]
    else:
        word_dict[char].append(index)
        

# Game start!
print("Guess the word! All letters are in lower cases. \n You have a total of {} tries.".format(str(tries)))
print("This is a {}-letter word".format(str(len(word))))

while word_dict:
    print("({} tries remaining)".format(str(tries)), " ".join(out), "\n")
    guess = input('Please guess a letter: ').lower()
    
    if guess in guessed:
        repeat += 1
        print("You have guessed this letter. Try a different one. \n")
        
        if repeat == repeat_allowed:
            print("You guessed repeated letter too many times. \n")
            break
            
        continue
        
    if word_dict.get(guess):
        guessed.add(guess)
        for i in word_dict[guess]:
            out[i] = guess
        word_dict.pop(guess)
        
        if not word_dict:
            print("\n Congratulations!!! You got the word '{}'!".format(word))
            break
        
        print("Nice!")
        print("=================================")
    
    else:
        tries -= 1
        if tries == 0:
            print("Game Over. \n")
            print("The answer is '{}'.".format(word))
            break
        
        guessed.add(guess)
        print("Nope :(")
        print("=================================")

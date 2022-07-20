import random

def guessing_game(nRangeLower, nRangeUpper):
    print (f"Guess my number, it is between {nRangeLower} and {nRangeUpper}")
    has_guessed_correctly = False
    r = int(random.randint(nRangeLower, nRangeUpper))
    while has_guessed_correctly == False:
        guess = int(input("Input a number: "))
        if guess < r:
            print("My number is higher, guess again.")
        elif guess > r:
            print("My number is lower, guess again.")
        elif guess == r:
            print("You got it!")
            has_guessed_correctly = True

def process_word(word):
    word = word.lower().replace(" ", "")
    return word

def is_anagram(word_one, word_two):
    word_one_processed = process_word(word_one)
    word_two_processed = process_word(word_two)
    if sorted(word_one_processed) == sorted(word_two_processed):
        print ("These words are anagrams.")
        return True
    else:
        print ("These words are not anagrams")
        return False


is_anagram("Tar", "rAt")
guessing_game(20, 50)



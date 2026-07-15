# === CS 115 Homework 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Brooke Hughes
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 2 ===
morse = (
    ('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'), ('-..', 'D'), ('.', 'E'),
    ('..-.', 'F'), ('--.', 'G'), ('....', 'H'), ('..', 'I'), ('.---', 'J'),
    ('-.-', 'K'), ('.-..', 'L'), ('--', 'M'), ('-.', 'N'), ('---', 'O'),
    ('.--.', 'P'), ('--.-', 'Q'), ('.-.', 'R'), ('...', 'S'), ('-', 'T'),
    ('..-', 'U'), ('...-', 'V'), ('.--', 'W'), ('-..-', 'X'), ('-.--', 'Y'),
    ('--..', 'Z')
)

dictionary = ("AM", "AS", "BE", "BED", "CAN", "EGG", "HE", "HER", "HIM",
    "HIS", "ILL", "IS", "KID", "ME", "MY", "ON", "OR", "SEE", "SO", "TO",
    "TOE", "TOW", "WAS", "WOW",)

#from dict import dictionary
#from bigdict import dictionary

def encode(plaintext):
    '''
    Takes a fully capitalized english word as a string and converts it into morse code
        Args:
            plaintext (string): fully capitalized english word
        Returns:
            (string): encoded morse code with spaces between each character
    '''

    # if there is no more text to translate, return nothing and end the loop
    if len(plaintext) == 0:
        return ""
    
    # get the morse code match to the first character in the plaintext
    morse_code = morse_lookup(plaintext[0], 0)

    # return first encoded plaintext character and the remaining plaintext to be encoded
    if len(plaintext) == 1:
        return morse_code
    return morse_code + " " + encode(plaintext[1:])


def morse_lookup(letter, num):
    '''
    Cycles through a morse code dictionary to find and return the morse equivalent to the letter
        Args:
            letter (string): capitalized english letter meant to be translated into morse code
            num (int): helps cycle through the morse code dictionary (should always be =0)
        Returns:
            (string): morse code equivalent of letter
    '''

    if num >= len(morse):
        return "?"
    # if letter is in this particular iteration of morse dictionary, return its morse code equivalent
    if letter == morse[num][1]:
        return morse[num][0]
    # otherwise continue to cycle through the tuple dictionary
    else:
        return morse_lookup(letter, num + 1)



def decode(cyphertext):
    '''
    Takes morse code separated by spaces and converts it into a fully capitalized english word
        Args:
            cyphertext (string): morse code separated by spaces
        Returns:
            (string): decoded fully capitalized english word
    '''

    # if there is no more cyphertext to decode, end the loop
    if len(cyphertext) == 0:
        return ""
    
    # gets the english character match to the first portion of morse code
    text, cyphertext = letter_lookup(cyphertext, 0)

    # returns the first decoded cyphertext character and the remaining cyphertext to be decoded
    return text + decode(cyphertext)


def letter_lookup(code, num):
    '''
    Takes a sting of several morse characters separated by a space and converts the first one its corresponding english character  
        Args:
            code (string): morse characters separated by spaces
            num (int): helps cycle through morse code dictionary (should always be =0)
        Returns:
            (string): the corresponding english character of the first morse character in the string
            (string): the remaining morse code to be decoded
        
    '''
    
    # split the encoded morse into a list of its individual letters
    split_cypher = code.split()

    if num >= len(morse):
        return "?", " ".join(split_cypher[1:])

    # if cypher is found in dictionary, return its english equivalent and the remaining cyphertext to decode
    if split_cypher[0] == morse[num][0]:
        return morse[num][1], " ".join(split_cypher[1:])
    # else continue to cycle through the dictionary
    else:
        return letter_lookup(code, num + 1)
    


def matches(cyphertext):
    '''
    Returns the possible words a string containing morse code without spaces could represent
        Args:
            cyphertext (string): morse code word without spaces
        Returns:
            (list): possible words that the cyphertext could be representative of
    '''
    return list(filter(lambda word: word_to_morse_no_space(word) == cyphertext, dictionary))


def word_to_morse_no_space(word):
    '''
    Converts a word to morse code and deletes all of the spaces in it
        Args:
            word (string): any fully capitalized english word
        Returns:
            (string): morse code equivalent without spaces
    '''
    encoded_word = encode(word)
    return encoded_word.replace(" ", "")
    
#!/usr/bin/env python3

import sys

""" Find the compound percent by using a simple algorithm"""

USAGE = '''
Cunter

USAGE:
    {script_name} name_of_text_file.txt number_of_repeated_words

example: $chmod +x counter.py
$./counter.py shakespear.txt 50
end
'''

USAGE = USAGE.strip()

def counter(filename:str):
    #no arguments provided -- print USAGE and exit with error 
    if len(filename) <= 1 or len(filename) <=2 or len(filename) >=4 :
        print(USAGE)
        exit(-1)

    #print arguments and len of them to know
    print(f'Received args: {filename}, {len(filename)}')

    #took my args to my variables
    script_name = filename[0]
    file = open(filename[1], 'r')
    repeat = filename[2]
    #read a text file
    text = file.read()
    # create a dictionary
    count = dict()
    # format the text and clear the words for using it in my counter
    words = text.split()
    #remove unneeded symbols
    remove_characters = str.maketrans('', '', '@#$!?&=+<>|;.-,[](){}:1234567890\'\\/"')
    l = [s.translate(remove_characters) for s in words]
    #all letters in the list of words get lower
    l = [ word.lower() for word in l ]
    # for cycle, the counter
    for word in l:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    # for cycle which types only the words that
    # repeated number_of_repeated_words
    for k, v in count.items():
        if v == int(repeat):
            print(f'Word: {k}, that repeated: {v} times.\n')
    

if __name__ == '__main__':
    counter(sys.argv)

    



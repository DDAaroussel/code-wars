#! python3

def getCount(inputStr):
    num_vowels = 0
    compressed = inputStr.replace(' ','')
    for i in compressed:
        if i in 'aeiou':
            num_vowels =+ num_vowels + 1
    return num_vowels

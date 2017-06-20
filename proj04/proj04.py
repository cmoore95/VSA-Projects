# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

#shortcut


phrase=raw_input('Enter a word or phrase. ')
length=len(phrase)
end=phrase[1:]

phrase=phrase.lower()

if phrase==phrase[::-1]:
    print phrase[0].upper()+end,'is a palindrome'
else:
    print phrase[0].upper()+end,'is not a palindrome'


# Name: Carter Moore
# Date: 6-19-17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name=raw_input('Enter your name: ')
age = int(raw_input('How old are you? '))
birth = raw_input('Have you had a birthday this year? ')
yes = True
no = False
if (2017-age+100) > 100 and birth == no:
    print name, 'will be 100 years old in', (2017-age+100)
elif (2017-age+100) > 100:
    print name, 'will be 100 years old in', (2017-age+99)
else:
    print name, 'was 100 years old in', (2017-age+100)

# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")

if birthday == 'Y':
    year=2017
elif birthday == 'N':
    year=2016

while age < 100:
    age=age +1
    year=year+1
    print year

print name,' will turn 100 in', year

# Name: Carter Moore
# Date: 6-19-17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name=raw_input('Enter your name: ')
age = int(raw_input('How old are you? '))
birth = raw_input('Have you had a birthday this year? ')
end_slice = name[1:]
if age < 100 and birth == 'no' or 'No' or 'n' or 'N':
    print name[0].upper()+end_slice, 'will be 100 in', (2017-age+99)
elif age < 100 and birth == 'yes' or 'Yes' or 'y' or 'Y':
    print name[0].upper()+end_slice, 'will be 100 in', (2017-age+100)
elif age > 100 and birth == 'no' or 'No' or 'n' or 'N':
    print name[0].upper()+end_slice, 'was 100 in', (2017-age+99)
else:
    print name[0].upper()+end_slice, 'was 100 in', (2017-age+100)
if age > 17:
    print 'You can watch movies rated R, PG-13, PG, and G'
elif age > 12:
    print 'You can watch movies rated PG-13, PG, and G'
elif age > 5:
    print 'You can watch movies rated PG, and G'
else:
    print 'You can watch movies rated G'

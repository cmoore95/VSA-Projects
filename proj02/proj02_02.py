# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""


total=int(raw_input('How many Fibonacci numbers would you like? '))

number=1
cur=1
prev=1
while total < (total + 1):
    total = total + 1
    cur=cur+prev
    print 
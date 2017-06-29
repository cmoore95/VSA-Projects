# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""


total1 = int(raw_input('How many Fibonacci numbers would you like (FOR Loop)? '))

number1 = 0
current1 = 1
previous1 = 0
old1 = previous1 + current1
for number1 in range(total1):
    old1 = current1
    print current1
    current1 = current1 + previous1
    previous1 = old1


total2 = int(raw_input('How many Fibonacci numbers would you like (WHILE Loop)? '))

number2 = 0
current2 = 1
previous2 = 0
old2 = previous2 + current2
while number2 < total2:
    old2 = current2
    print current2
    current2 = current2 + previous2
    previous2 = old2
    number2 = number2 + 1


total3 = int(raw_input('How many powers of 2 would you like? '))

number3 = 1
current3 = 1
previous3 = 2
while number3 < (total3 + 1):
    current3 = current3 * previous3
    number3 = number3 + 1
    print current3


total4 = int(raw_input('What number do you want the divisors of? '))

number4=1
answer4=0
while number4<(total4+1):
    if total4%number4==0:
        answer4=total4/number4
        print answer4
    number4=number4+1

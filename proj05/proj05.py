# Name:
# Date:

# proj05: functions and lists

# Part I



def divisors(num):
    total=num
    number=1
    answer=0
    list1 = []
    while number<(total+1):
        if total%number==0:
            answer=(total/number)
            list1.append(answer)
        number=number+1
    print 'The divisors of',num,'are',list1[::-1]
    return list1[::-1]


#    """
#    Takes a number and returns all divisors of the number, ordered least to greatest
#    :param num: int
#    :return: list (int)
#    """


def prime(num):
    divisor_list=divisors(num)
    length=len(divisor_list)
    if length==2:
        print "Congrats", num, "is a prime, divisors are ", divisor_list
        return True
    else:
        print "your number", num, "is not a prime"
        return False

#    """
#    Takes a number and returns True if the number is prime, otherwise False
#    :param num: int
#    :return: bool
#    """


# Part II

def intersection(lst1, lst2):
    if len(lst1)>len(lst2):
        big_list=lst1
        small_list=lst2
    else:
        big_list=lst2
        small_list=lst1
    final_list=[]
    for letter in small_list:
        if letter in big_list:
            final_list.append(letter)
    print 'These numbers are common between the lists',final_list
    return final_list



#L1=[]
#L2=[3,4]
#L3=[3,'a']
#L4=[5,'b',10,7,'a']
#L5=[5,7,11]


#    """
#    Takes two lists and returns a list of the elements in common between the lists
#    :param lst1: list, any type
#    :param lst2: list, any type
#    :return: list, any type
#    """
#    return ["test"]

# Part III

def find_ab(side1, side2, side3):
    a=1
    b=1
    if side1>side2 and side1>side3:
        a=side2
        b=side3
    elif side2>side1 and side2>side3:
        a=side1
        b=side3
    else:
        a=side1
        b=side2
    sides=[a,b]
    print a,'and',b,'are sides a and b'
    return sides

#    """
#    Takes three side lengths an returns two smallest in a list
#    :param side1: int or float
#    :param side2: int or float
#    :param side3: int or float
#    :return: list of 2 ints or floats
#    """
#    return [0, 0]


def find_c(side1, side2, side3):
    c=0
    if side1>side2 and side3:
        c=side1
    if side2>side1 and side3:
        c=side2
    if side3>side1 and side2:
        c=side3
    print c,'is side c'
    return c

#    """
#    Takes three side lengths an returns the largest
#    :param side1: int or float
#    :param side2: int or float
#    :param side3: int or float
#    :return: int or float
#    """
#    return 0

def square(side):
    square_ans=side*side
    print square_ans,'is the square of that number.'
    return square_ans

#    """
#    Takes a side length and returns the side length squared
#    :param side: int or float
#    :return: int or float
#    """
#    return 0

def pythagorean(a,b,c):
    if (a*a)+(b*b)==(c*c):
        print "That fits Pythagoras' Theorem"
        return True
    else:
        print "That doesn't fit Pythagoras' Theorem"
        return False

#    """
#    Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
#    :param a: int or float
#    :param b: int or float
#    :param c: int or float
#    :return: bool
#    """
#    return False

def is_right(side1, side2, side3):
        ab=find_ab(side1,side2,side3)
        c=find_c(side1,side2,side3)
        add=(ab[0]*ab[0])+(ab[1]*ab[1])
        if add==c*c:
            print "This is a right triangle"
            return True
        else:
            print 'Nope, not a right triangle'
            return False

#    """
#    Takes three side lengths and returns true if triangle is right
#    :param side1: int or float
#    :param side2: int or float
#    :param side3: int or float
#    :return: bool
#    """
#    return False

# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS")
else:
    print("Test 3: FAIL")

# Test 3.1
if divisors(16) == [1,2,4,8,16]:
    print("Test 3.1: PASS\n")
else:
    print("Test 3.1: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS")
else:
    print("Test 5: FAIL")

# Test 51
if prime(11):
    print("Test 51: PASS")
else:
    print("Test 51: FAIL")

# Test 52
if prime(16):
    print("Test 52: FAIL\n")
else:
    print("Test 52: PASS\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")

# Test 12.1
if is_right(6,8,10):
    print("Test 12.1: PASS")
else:
    print("Test 12.1: FAIL")

# Test 12.2
if is_right(6,13,14):
    print("Test 12.2: FAIL\n")
else:
    print("Test 12.2: PASS\n")

is_right(5,12,13)

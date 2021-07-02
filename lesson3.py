
def split_in_half(s):
    length = len(s)
    half = int(length / 2)
    add = 0
    if(length % 2):
        add = 1
    left = s[:half + add]
    right = s[half + add:]
    return right + left

def uni_char(s): #abcde
    my_set = set(s) #{a, b, c, d, e} length = 5
    return len(s) == len(my_set)

def square_num(numbers):
    sum = 0
    for number in numbers:
        print(number)
        sum += number * number
    return sum

def is_palindrome(s):
    for i in range(len(s)):
        subs = s[:i] + s[i +1:]
        print("Step: " + str(i) + ", Substring: " + subs)
        if subs == subs[::-1]:
            return True
    return s == s[::-1]

#Equation:
#F0 = 0
#F1 = 1
#f2 = 1
#fn = Fn-1 + Fn-2

def fibonacci(n):
    if n < 0:
        return "Not a valid value"
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    index = 3
    fib_1 = 1
    fib_2 = 1
    result = [fib_1, fib_2] #[1, 1]

    while index <= n: #index = 5, n = 7, fib_1 = 3, fib_2 = 3
        result.append(fib_1 + fib_2) #[1,1,2,3,5]
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        index += 1

    return result

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(split_in_half("aacbb")) #aacbb --> bbaac
print(split_in_half("aabb"))

print(uni_char("abcde")) #true
print(uni_char("aabhsad")) #false

print(square_num([1,2,2]))

print(is_palindrome("radar")) #true
print(is_palindrome("radir")) #false

print(fibonacci(7))

print(is_leap_year(2013))
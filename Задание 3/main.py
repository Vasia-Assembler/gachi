import re


def last_fib_digit(q):
    return ([1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1, 0]
            [q % 60 - 1]) # Due to the fact that in a sequence of Fibonacci numbers the last digits repeat every 60 time, we can make an O1 solution.

f = open('./input.txt', 'r')
s = f.read()
result = re.search(r'(?:-|)([0-9]+)', s)
number = int(result.group(0))
o = open('./output.txt', 'w')
o.write(str(last_fib_digit(number)) + '\n')


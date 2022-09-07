import re


def calc_fib(p):
    def iter(prev, counter, product):
        if (counter == 0):
            return product
        else:
            return iter(product, counter - 1, (product + prev))
    return iter(1, p, 0)

f = open('./input.txt', 'r')
s = f.read()
result = re.search(r'(?:-|)([0-9]+)', s)
number = int(result.group(0))
print(calc_fib(number))
o = open('./output.txt', 'w')
o.write(str(calc_fib(number)) + '\n')

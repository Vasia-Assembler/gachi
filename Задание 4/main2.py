import time
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
o = open('./output.txt', 'w')
t_start = time.perf_counter()
fib_result = calc_fib(number)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
o.write(str(fib_result) + '\n')
import re
f = open('./input.txt', 'r')
s = f.read()

result = re.search(r'(?:-|)([0-9]+)', s)
first = result.group(0)
second = result.group(1)
sum =  int(first) + int(second)

o = open('./output.txt', 'w')
o.write(str(sum) + '\n')

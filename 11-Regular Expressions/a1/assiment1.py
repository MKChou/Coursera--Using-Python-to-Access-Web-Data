import re


file = open("/Users/mkchou/Desktop/Using Python to Access Web Data/11-Regular Expressions/a1/numbers.txt")
text = file.read()
num = re.findall('[0-9]+',text)
total = 0
for i in num:
    i = int(i)
    a = a+ i;
print(a)

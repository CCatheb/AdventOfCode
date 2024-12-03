import re

with open("data.txt", "r") as file:
    data = file.read()

total = 0

for result in re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\))', data):
    numbers = re.findall(r'\d+', result)
    total = total + (int(numbers[0]) * int(numbers[1]))

print("Total amount is:", total)
    
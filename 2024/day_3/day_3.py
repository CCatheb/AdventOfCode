import re
import time

with open("data.txt", "r") as file:
    data = file.read()

start = time.time()
total = 0
for result in re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\))', data):
    numbers = re.findall(r'\d+', result)
    total = total + (int(numbers[0]) * int(numbers[1]))

print("Total amount is:", total)
end = time.time() - start
print(f"Took {end}s to execute.")

# Part 2

start = time.time()
# splitted_dont got all data (active and inactive)
# splitted_do got data on splitted_dont that is active
splitted_dont = data.split("don't()")
# Take the first one, as is is considered as active
splitted_do = [splitted_dont[0]] 
for element in splitted_dont[1:]:
    # Don't take the first, is is not active
    splitted_do.append(element.split("do()")[1:])

complete = ''.join(str(e) for e in splitted_do)
total = 0
for result in re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\))', complete):
    numbers = re.findall(r'\d+', result)
    total = total + (int(numbers[0]) * int(numbers[1]))

print("Total amount is:", total)
end = time.time() - start
print(f"Took {end}s to execute.")
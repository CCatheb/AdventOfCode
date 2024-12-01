import time

list_1 = []
list_2 = []

with open("data.txt", "r") as file:
    for line in file:
        data = line.split(" ")
        list_1.append(int(data[0]))
        list_2.append(int(data[-1].strip()))

total = 0

################ Part 1 ####################
start = time.time()
list_1.sort()
list_2.sort()

for i in range(len(list_1)):
    sum = abs(list_2[i] - list_1[i])
    total += sum
end = time.time() - start
print(f"Part 1 took {end}s to execute. Result is {total}")

total = 0

############### Part 2 ######################
start = time.time()
for i in list_1:
    sum = (list_2.count(i) * i)
    total += sum

end = time.time() - start
print(f"Part 2 took {end}s to execute. Result is {total}")


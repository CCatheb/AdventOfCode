list_1 = []
list_2 = []

with open("data.txt", "r") as file:
    for line in file:
        data = line.split(" ")

        list_1.append(int(data[0]))
        list_2.append(int(data[-1].strip()))

list_1.sort()
list_2.sort()
total = 0

for i in range(len(list_1)):
    sum = abs(list_2[i] - list_1[i])
    print(f"{list_2[i]} - {list_1[i]} = {sum}")
    total += sum

print(total)
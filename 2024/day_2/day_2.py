from typing import List
import time

reports = []

with open("data.txt", "r") as file:
    for line in file:
        report = [int(x) for x in line.split()]
        reports.append(report)

# Part 1 & 2
# We want to ensure that the list is increasing OR decreasing, 
# With no more than 3 units of increase or decrease

def is_safe(report) -> bool:

    def is_valid_sequence(seq) -> bool:
        # Check that all meets the requirements ( 0 < diff < 4, incr or decr)
        increasing = all(1 <= seq[i+1] - seq[i] <= 3 for i in range(len(seq) - 1))
        decreasing = all(1 <= seq[i] - seq[i+1] <= 3 for i in range(len(seq) - 1))
        return increasing or decreasing

    # In that case, the list is valid by default
    if is_valid_sequence(report):
        return True

    # Else, we have to check if the list is valid on each replacement
    # The first that match is the correct one, enough to say that report is safe
    for i in range(len(report)):
        # Can't use pop, otherwise it remove all elements from list
        modified_report = report[:i] + report[i+1:]
        if is_valid_sequence(modified_report):
            return True

    return False


start = time.time()
total = 0
for report in reports:
    if is_safe(report):
        total += 1

end = time.time() - start
print(f"{total} reports are safe.\nTook {end}s to execute.")

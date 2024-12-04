with open("data.txt", "r") as file:
    data = [list(row.strip()) for row in file.readlines()]

# Directions as a delta (row, column)
DIRECTIONS = [
    (0, 1),  
    (0, -1),  
    (1, 0),  
    (-1, 0),  
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

def is_within_bounds(i: int, j: int, dr: int, dc: int, rows: int, cols: int) -> bool:
    """This methods checks if a direction is within grids bounds

    Args:
        i (int): Element i
        j (int): Element j
        dr (int): Row delta
        dc (int): Column delta
        rows (int): Number of rows
        cols (int): Number of columns

    Returns:
        bool: True if the direction is within bounds
    """

    return (
        0 <= i + 3 * dr < rows and
        0 <= j + 3 * dc < cols
    )

def find_xmas(data):
    rows, cols = len(data), len(data[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            for dr, dc in DIRECTIONS:
                if is_within_bounds(i, j, dr, dc, rows, cols):
                    if (
                        data[i][j] == "X" and
                        data[i + 1 * dr][j + 1 * dc] == "M" and
                        data[i + 2 * dr][j + 2 * dc] == "A" and
                        data[i + 3 * dr][j + 3 * dc] == "S"
                    ):
                        count += 1
    return count

print("Number of XMAS occurences:", find_xmas(data))

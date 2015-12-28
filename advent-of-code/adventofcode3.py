# http://adventofcode.com/day/3/

# keep track of houses with tuple coordinate points
# add/sub y axis for n/s
# add/sub x axis for e/w
# add coordinates to set as you go
# return length of set


def find_gifted_houses(filename):
    """Return number of houses visited/gifted"""
    house = (0, 0)
    visited = set()

    visited.add(house)

    for item in filename:
        if item == "^":
            house = (house[0], (house[1]+1))
        elif item == "v":
            house = (house[0], (house[1]-1))
        elif item == ">":
            house = ((house[0]+1), house[1])
        elif item == "<":
            house = ((house[0]-1), house[1])
        visited.add(house)

    return len(visited)


with open('input3.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

input_file = list(data)

print find_gifted_houses(input_file)

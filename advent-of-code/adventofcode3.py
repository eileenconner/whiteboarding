# http://adventofcode.com/day/3/

# keep track of houses with tuple coordinate points
# add/sub y axis for n/s
# add/sub x axis for e/w
# add coordinates to set as you go
# return length of set


def find_gifted_houses(filename):
    starting = (0, 0)
    visited = set()

    visited.add(starting)

    for item in filename:
        if item == "^":
            starting = (starting[0], (starting[1]+1))
        elif item == "v":
            starting = (starting[0], (starting[1]-1))
        elif item == ">":
            starting = ((starting[0]+1), starting[1])
        elif item == "<":
            starting = ((starting[0]-1), starting[1])
        visited.add(starting)

    return len(visited)


with open('input3.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

input_file = list(data)

print find_gifted_houses(input_file)

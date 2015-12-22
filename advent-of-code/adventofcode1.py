# http://adventofcode.com/day/1


def find_floor_number(floors):
    """Find floor number from data in file"""
    floor = 0
    count = 0

    for item in floors:
        if item == "(":
            floor += 1
        elif item == ")":
            floor -= 1

        # id when santa reaches floor -1
        count += 1
        if floor == -1:
            print "Floor -1: ", count

    return floor

# open file, read into string, split into list, & run fn
with open('input1.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

floors = data.split()

print find_floor_number(data)

myfile.close()

# http://adventofcode.com/day/2


def find_paper_amt(filename):
    """Find total area of paper to wrap boxes"""
    total_paper = 0

    for line in filename:
        data = extract_file_data(line)

        # per line, find 2*l*w + 2*w*h + 2*h*l + smallest side area
        side1 = data[0] * data[1]
        side2 = data[1] * data[2]
        side3 = data[2] * data[0]

        smallest = min(side1, side2, side3)

        paper = 2 * (side1 + side2 + side3) + smallest

        # increment total amt of paper
        total_paper += paper

    return total_paper


def find_ribbon_amt(filename):
    """Find total length of ribbon required"""
    total_ribbon = 0

    for line in filename:
        data = extract_file_data(line)

        # per line, find smallest perimeter of any one face
        ordered_sides = sorted(data)
        perimeter = 2 * (ordered_sides[0] + ordered_sides[1])

        # find cubic volume of cube
        volume = data[0] * data[1] * data[2]

        ribbon = perimeter + volume

        # increment total amount of ribbon
        total_ribbon += ribbon

    return total_ribbon


def extract_file_data(line):
    # extract data and transform into int form
    data = line.split("x")

    length = int(data[0])
    width = int(data[1])
    height = int(data[2])

    return [length, width, height]


input_file = open("input2.txt", "r")

print find_paper_amt(input_file)
print find_ribbon_amt(input_file)

input_file.close()

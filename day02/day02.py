def read(clean_func):
    with open("input.txt") as file:
        input = file.readlines()
    return clean_func(input)


def clean(input):
    lists = []
    for line in input:
        entry = [int(i) for i in line.split()]
        lists.append(entry)
    return lists


def asc_dsc(line):
    asc, desc = 0, 0
    steps = len(line) - 1
    for i in range(steps):
        diff = line[i] - line[i + 1]
        if -4 < diff < 0:
            asc += 1
        if 0 < diff < 4:
            desc += 1
    if asc == steps or desc == steps:
        return True
    return False


def checkdrop(line):
    for i in range(len(line)):
        safe = list(line)
        safe.pop(i)
        if asc_dsc(safe):
            return True
    return False


def part1():
    count = 0
    for line in read(clean):
        if asc_dsc(line):
            count += 1
    print("count: ", count)


def part2():
    count = 0
    for line in read(clean):
        if asc_dsc(line):
            count += 1
        elif checkdrop(line):
            count += 1
    print("count: ", count)


part2()

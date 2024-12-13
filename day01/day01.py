def read(clean_func):
    with open("input.txt") as file:
        input = file.readlines()
    return clean_func(input)


def clean(input):
    lists = {"a": [], "b": []}
    for line in input:
        entry = line.split()
        lists["a"].append(int(entry[0]))
        lists["b"].append(int(entry[1]))
    return lists


def sort_lists(sorted):
    sorted["a"].sort()
    sorted["b"].sort()
    return sorted


def part1():
    input = read(clean)
    sorted = sort_lists(input)
    diff = 0
    for a, b in zip(sorted["a"], sorted["b"]):
        diff += abs(a - b)
    print(diff)


def part2():
    input = read(clean)
    sum = 0
    for num in input["a"]:
        sum += input["b"].count(num) * num
    print(sum)


part1()

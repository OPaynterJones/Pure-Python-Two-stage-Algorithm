import string
import math

k = 4


def reorder(list, start_index):
    start_index -= 1
    for i in range(start_index + 1, len(list)):
        yield list[i]
    for i in range(0, start_index):
        yield list[i]


def circular(input):
    while True:
        for i in input:
            yield i


def depth_gen(data, indicies):
    data = list(data)
    new = []
    for _ in range(len(data)):
        new.append(data.pop(next(indicies)))

    newsubindex = []
    for i, letter in enumerate(new):
        newsubindex.append([letter, (i // 2) + 1])
    return newsubindex


def P(depth, k):
    PsubGeneration = math.pow(math.e, (-depth / k))
    return PsubGeneration


letters = [i for i in string.ascii_lowercase]
indicies = circular([0, -1])
data = reorder(letters, 3)
new = depth_gen(data, indicies)
for node in new:
    node[1] = P(node[1], k)
print(new)

# TODO: Use new function to guarantee binding to adjacent to one another
# TODO: Use UUID to generate many new nodes and pass then through the graph algorithm mentioned above
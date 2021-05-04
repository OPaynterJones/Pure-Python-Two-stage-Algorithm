import string
import math
import matplotlib.pyplot as plt
import random

# k = 3
# D 5.0 where k = 3
# D 6.8 where k = 4
# D 8.3 where k = 5
letter_code = dict(zip(string.ascii_lowercase, range(1, 26)))
letter = "a"
lettersubcode = letter_code[letter]


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


def depth_gen(data):
    indicies = circular([0, -1])
    new = []
    for _ in range(len(data)):
        new.append(data.pop(next(indicies)))

    newsubindex = []
    for i, letter in enumerate(new):
        newsubindex.append([letter, (i // 2) + 1])
    return newsubindex


def Panalysis(k):
    y = []
    for i in range(0, 26):
        y.append(math.pow(math.e, (-i / k)))
    plt.figure(1)
    plt.subplot(111)
    plt.plot(range(0, 26), y)
    plt.show()

    for node in nodes_probability:
        print(node[0], node[1] * 100)


def P(depth, k):
    PsubGeneration = math.pow(math.e, (-depth / k))
    return PsubGeneration


letter_code = [i for i in string.ascii_lowercase]

data = list(reorder(letter_code, lettersubcode))
nodes_probability = depth_gen(data)

# for node in nodes_probability:
#     node[1] = P(node[1], k)

#

# TODO: Use new function to guarantee binding to ad jacent to one another
# TODO: Use UUID to generate many new nodes and pass then through the graph algorithm mentioned above

print("\n\n\n\n\n")
averages = []
for k in range(1, 10):
    Panalysis(k)
    for node in nodes_probability:
        node[1] = P(node[1], k)
    total = 0
    sample = 100000
    for _ in range(sample):
        network = {letter: [arc for arc, P in nodes_probability if random.randint(0, 100) <= (P*100)]}
        # print(len(network[letter]), network[letter])
        total += len(network[letter])

    average = total/sample
    print(average)
    averages.append(average)
print(averages)

# network = {letter: []}
# for arc, P in nodes_probability:
#     rand = random.randint(0, 100)
#     print(rand, arc, P*100)
#     if rand <= P*100:
#         network[letter].append(arc)
#         print(rand, "^^^^")
# print(network)

# for node, probability in nodes_probability:  #
#     rand = random.randint(0, 10)
#     print(rand, probability * 100)
#     if rand <= probability * 100:
#         network[letter].append(node)
#
# print(network)

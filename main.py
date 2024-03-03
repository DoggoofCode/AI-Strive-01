# let x be house sizes
x = [i for i in range(1000, 3001, 500)]
scaled_x = [x_value / 1000 for x_value in x]
# let y be house prices
y = [k for k in range(50_000, 150_001, 25_000)]


class network:
    def __init__(self, gr=0, yi=0):
        self.m = gr
        self.c = yi

    def findDevianceWH(self, inp, out): return abs(((self.m + H) * inp + self.c) - out)

    def findDeviance(self, inp, out): return abs((self.m * inp + self.c) - out)


def Cost(Network: object, inp: list, out: list) -> float:
    try:
        tCost = 0
        for i in range(len(inp)):
            tCost += Network.findDeviance(inp[i], out[i])
        return tCost / len(inp)
    except IndexError:
        return 0.0


def CostWH(Network: object, inp: list, out: list) -> float:
    try:
        tCost = 0
        for i in range(len(inp)):
            tCost += Network.findDevianceWH(inp[i], out[i])
        return tCost / len(inp)
    except IndexError:
        return 0.0


print(x)
print(y)
n = network(0, 0)

LEARN_RATE = 0.000001
EPOCHS = 100000
H = 0.0001
print(len(scaled_x) == len(y))

for _ in range(EPOCHS):
    slope = (Cost(n, x, y) - CostWH(n, x, y)) / H
    n.m += slope * LEARN_RATE

print(f"M = {n.m}, C = {n.c}")


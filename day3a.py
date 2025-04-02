file = open("./data/day3.txt", "r")
input = file.read()

class Sink:
    def __init__(self, input):
        self.input = input
        self.index = 0
    def is_full(self):
        return self.index == len(self.input)
    def consume(self, char: str):
        if self.index < len(self.input) and self.input[self.index] == char:
            self.index += 1
        else: self.index = 0
    

mul_sink = Sink("mul(")

def parse_number(x: str, i: int):
    if len(x) == 0 or not x[i].isdigit(): return None, i
    start = i
    while x[i].isdigit(): i += 1
    num = int(x[start:i])
    return num, i

total = 0

for i in range(0, len(input)):
    mul_sink.consume(input[i])
    if not mul_sink.is_full(): continue

    i += 1
    first, i = parse_number(input, i)
    if first == None or input[i] != ",": continue

    i += 1
    second, i = parse_number(input, i)

    if input[i] != ")": continue

    total += first * second

print(total)

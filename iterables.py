# samp_str = iter("Sample")

# print("Char:", next(samp_str))
class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]

alpha = Alphabet()
for letter in alpha:
    print(letter)

derek = {"f_name": "Derek", "l_name": "Banas"}
for key in derek:
    print(key, derek[key])


class Fib_Generator:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_num = self.first + self.second
        self.first = self.second
        self.second = fib_num
        return fib_num

fib_seq = Fib_Generator()

for i in range(10):
    print("Fib:", next(fib_seq))

class Byte:
    def __init__(self, s=""):
        if s == "":
            self.array = [0 for _ in range(8)]
        else:
            self.array = [int(c) for c in s]

    def __str__(self):
        st = [str(c) for c in self.array]
        return "".join(st)

    def __lshift__(self, other):
        for i in range(other):
            self.array.pop(0)
            self.array.append(0)

    def __rshift__(self, other):
        for i in range(other):
            self.array.pop()
            self.array.insert(0, 0)

    def __and__(self, other):
        new_byte = Byte("")
        for i in range(8):
            new_byte.array[i] = self.array[i] & other.array[i]
        return new_byte

    def __or__(self, other):
        new_byte = Byte("")
        for i in range(8):
            new_byte.array[i] = self.array[i] | other.array[i]
        return new_byte

    def __xor__(self, other):
        new_byte = Byte("")
        for i in range(8):
            new_byte.array[i] = self.array[i] ^ other.array[i]
        return new_byte

    def __invert__(self):
        new_byte = Byte("")
        for i in range(8):
            new_byte.array[i] = 1 if self.array[i] == 0 else 0
        return new_byte

    def __len__(self):
        return 8

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value


b = Byte()
b2 = Byte("00010011")
print(b, b2)

"""b2 << 2
print(b2)"""

b2 >> 2
print(b2)

b2 = Byte("00010011")
b3 = Byte("00110101")
print(f"\n{b2}\n{b3}(&)\n{'-' * 8}\n{b2 & b3}")
print(f"\n{b2}\n{b3}(|)\n{'-' * 8}\n{b2 | b3}")
print(f"\n{b2}\n{b3}(^)\n{'-' * 8}\n{b2 ^ b3}")
print(f"\n{b3}(~)\n{'-' * 8}\n{~b3}")

for bit in b3:
    print(bit)

b3[0] = 1
print(b3)

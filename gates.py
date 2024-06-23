
# a and b must only be an array of size 0


def or_gate_64_bit(a, b):
    res = [None] * 64
    for i in range(64):
        res[i] = a[i] or b[i]
    return res

def or_gate(a, b):
    return a or b


def and_gate_64_bit(a, b):
    res = [None] * 64
    for i in range(64):
        res[i] = a[i] and b[i]
    return res

def and_gate(a, b):
    return a and b

def not_gate_64_bit(input):
    res = [None] * 64
    for i in range(64):
        res[i] = not input[i]
    return res

def xor_gate_64_bit(a, b):
    res = [None] * 64
    for i in range(64):
        res[i] = a[i] ^ b[i]
    return res


def xor_gate(a, b):
    return a ^ b


def mux(a, b, sel):
    if sel == 0:
        return a
    return b

def dmux(input, sel):
    if sel == 0:
        return (input, 0) # return a tuple of a = input, b = 0
    return (0, input) # return a tuple of a = 0, b = input


        





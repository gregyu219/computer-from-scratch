from hardware.gates import or_gate, and_gate, not_gate, full_adder

# 16 bit chips
# All inputs must be an array of length 16
def or_gate_16_bit(a, b):
    res = [None] * 16
    for i in range(16):
        res[i] = or_gate(a[i], b[i])

def and_gate_16_bit(a, b):
    res = [None] * 16
    for i in range(16):
        res[i] = and_gate(a[i], b[i])

def not_gate_16_bit(input):
    res = [None] * 16
    for i in range(16):
        res[i] = not_gate(input[i])

#  both a and b must be array size 16
#  overflow not handled
def adder_16_bit(a, b):
    res = [None] * 16
    carry = 0
    for i in reversed(range(16)):
        (res[i], carry) = full_adder(a[i], b[i], carry)

    return res

#  both a and b must be array size 4
def adder_4_bit(a, b):
    res = [None] * 4
    carry = 0
    for i in reversed(range(4)):
        (res[i], carry) = full_adder(a[i], b[i], carry)

    return res








# Tests
# print(half_adder(1,1))
# print(full_adder(1,1,1))

# a = [1,1,1,1]
# b = [0,0,0,1]
# print(adder_4_bit(a, b))
from gates import or_gate, xor_gate, and_gate

# return sum, carry
def half_adder(a, b):
    sum = xor_gate(a, b)
    carry = and_gate(a, b)
    return (sum, carry)

# return sum, carry
def full_adder(a, b, carry_input):
    first_sum, first_carry = half_adder(a, b)
    (second_sum, second_carry) = half_adder(first_sum, carry_input)
    carry_output = or_gate(first_carry, second_carry)
    return (second_sum, carry_output)

#  both a and b must be array size 16
def adder_4_bit(a, b):
    res = [None] * 4
    carry = 0
    for i in reversed(range(4)):
        (res[i], carry) = full_adder(a[i], b[i], carry)

    return res

#  both a and b must be array size 16
def adder_16_bit(a, b):
    res = [None] * 16
    carry = 0
    for i in reversed(range(16)):
        (res[i], carry) = full_adder(a[i], b[i], carry)

    return res










# Tests
# print(half_adder(1,1))
# print(full_adder(1,1,1))

# a = [1,1,1,1]
# b = [0,0,0,1]
# print(adder_4_bit(a, b))
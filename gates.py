def or_gate(a, b):
    return a or b

def and_gate(a, b):
    return a and b

def xor_gate(a, b):
    return a ^ b

def not_gate(input):
    return not input

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

def mux(a, b, sel):
    if sel == 0:
        return a
    return b

def dmux(input, sel):
    if sel == 0:
        return (input, 0) # return a tuple of a = input, b = 0
    return (0, input) # return a tuple of a = 0, b = input


        





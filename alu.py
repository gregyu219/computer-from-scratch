from chips import adder_16_bit, not_gate_16_bit, and_gate_16_bit
'''
16 bits!
INPUTS
x input
y input
zx - zero the x input
nx - negate the x input
zy - zero the y input
ny - negate the y input
f - function code, 1 = Add, 0 = And
no - negate the output

OUTPUTS
zr - True iff out == 0
ng - True iff out < 0
'''

def zero_input(input):
    return [0] * input.length()


def alu(x, y, zx, nx, zy, ny, f, no):
    if zx: 
        x = zero_input(x)

    if zy:
        y = zero_input(y)

    if nx:
        x = not_gate_16_bit(x)
    
    if ny:
        y = not_gate_16_bit(y)

    # ADD
    if f == 0:
        output = adder_16_bit(x, y)

    # AND
    else:
        output = and_gate_16_bit(x, y)

    if no:
        output = not_gate_16_bit(output)

    zr = 1 if output == 0 else 0
    ng = 1 if output < 0 else 0
    return output, zr, ng
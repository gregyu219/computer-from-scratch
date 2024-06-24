from hardware.chips import adder_16_bit, not_gate_16_bit, and_gate_16_bit
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
output[16]
zr - True iff out == 0 flag
ng - True iff out < 0
'''

### ALU functions ###


### End of ALU functions ###


### ALU implementation
def alu_16_bit(x, y, zx, nx, zy, ny, f, no):
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

    zr = 1 if check_zr(output) else 0
    ng = 1 if check_ng(output) else 0
    return output, zr, ng

def zero_input(input):
    return [0] * input.length()

def check_zr(output):
    for i in range(len(output)):
        if output[i] == 1:
            return 0
        
    return 1

def check_ng(output):
    return output[0] == 1

# a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# b = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# c = [1] * 16
# print(alu_16_bit(a, c, 0, 0, 0, 0, 0, 0))
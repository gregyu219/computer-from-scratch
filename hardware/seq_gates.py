class Register_16_bit:
    def __init__(self):
        self.data = [0] * 16

    # input is array length 16, load is boolean
    def load(self, input, load):
        if load and len(input) == 16:
            self.data = input

class Ram_8:
    def __init__(self):
        self.memory = [None] * 8
        for i in range(len(self.memory)):
            self.memory[i] = Register_16_bit()
    

    # input is array length 16, load is boolean
    def write(self, input, address, load):
        if load:
            self.memory[address].load(input, True)

class Ram_16k:
    def __init__(self):
        self.memory = [None] * 16384
        for i in range(len(self.memory)):
            self.memory[i] = Register_16_bit()

    

    # input is array length 16, load is boolean
    def write(self, input, address, load):
        if load:
            self.memory[address].load(input, True)


class Program_counter:
    def __init__(self):
        self.count = Register_16_bit()


# ram = Ram_8()
# new_data = [1] * 16
# ram.write(new_data,2,True)

# print(ram.memory[1].data)
# print(ram.memory[2].data)
# print(ram.memory[3].data)





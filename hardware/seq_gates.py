class Register_16_bit:
    def __init__(self):
        self.data = [None] * 16

    # input is array length 16, load is boolean
    def load(self, input, load):
        if load:
            self.data = input

class Ram_8:
    def __init__(self):
        self.memory = [Register_16_bit()] * 8
    

    # input is array length 16, load is boolean
    def write(self, input, address, load):
        if load:
            self.memory[address].load(input, True)

class Ram_16k:
    def __init__(self):
        self.memory = [Register_16_bit()] * 16384
    

    # input is array length 16, load is boolean
    def write(self, input, address, load):
        if load:
            self.memory[address].load(input, True)


class Program_counter:
    def __init__(self):
        self.count = Register_16_bit()





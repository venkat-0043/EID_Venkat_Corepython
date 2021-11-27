class Laptop(object):
    # stores the laptop details

    # STATE
    def __init__(self, ram, rom, processor, graphic_card):
        # initializing the instance attributes
        self.ram = ram
        self.rom = rom
        self.processor = processor
        self.graphic_card = graphic_card

    # BEHAVIOUR
    def get_ram(self):
        # return the RAM capacity
        return self.ram

    def get_rom(self):
        # returns the ROM capacity
        return self.rom

    def get_processor(self):
        # returns the processor type
        return self.processor

    def get_graphic_card(self):
        # returns the graphic card type
        return self.graphic_card


l = Laptop('8 GB', '512 GB', 'intel i5', 'NVIDIA')

print("ram is : ", l.get_ram())
print("rom is : ", l.get_rom())
print("processor is : ", l.get_processor())
print("graphic card is : ", l.get_graphic_card())


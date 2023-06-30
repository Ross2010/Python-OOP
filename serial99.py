"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 100):
        self.serial = start

    def generate(self):
        serial = self.serial
        self.serial +=1
        return serial

    def reset(self):
        self.serial = 100

serial = SerialGenerator()
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
serial.reset()
print(serial.generate())
print(serial.generate())

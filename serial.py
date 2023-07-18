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
    def __init__(self,start=100):
        self.start=start
        self.has_run=False

    def generate(self):
        if self.has_run:
            self.start +=1
        self.has_run = True
        return self.start

    def reset(self):
        self.start = 100
        self.has_run =False



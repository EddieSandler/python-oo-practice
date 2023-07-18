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

    def __init__(self, start):
        """Defines   serialGenerator   properties. sets initial
        value to 100 and flag indicating whether the generate function
        has run .(initially False)

        """
        self.start = start
        self.num=start
        self.has_run = False

    def generate(self):
        """ Function that increments the serialGenerator value by 1 if it
        hasn't run  previously.  Sets the has_run flag to True if it has run
        previously.

        """
        if self.has_run:
            self.num += 1
        self.has_run = True
        return self.num

    def reset(self):
        """Function to reset the serial generator back
        to its default value (100)"""

        self.num = self.start
        self.has_run = False

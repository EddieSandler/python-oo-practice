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
        value to whatever is passed and flag indicating
        whether the generate function has run .(initially False)
        """
        self.start = start
        # naming convention
        self.generated_num = None
        # self.has_run = False

    def generate(self):
        """ Function that increments the serialGenerator value by 1 if it
        hasn't run  previously.  Sets the has_run flag to True if it has run
        previously.

        """
        if not self.generated_num:
            self.generated_num = self.start
            return self.start
        else:
            self.generated_num += 1
            return self.generated_num

        # if self.has_run:
        #     self.generated_num += 1
        # self.has_run = True
        # return self.generated_num

    def reset(self):
        """Function to reset the serial generator back
        to its default value"""

        self.generated_num = None
        # self.has_run = False

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

    #TODO: write __repr__
    def __repr__(self):
        return f"<serial current={self.current}, original={self.original}>"

    """initialize serial with a start number, then set current and original to start"""
    def __init__(self, start=100):
        self.current = start
        self.original = start

    """returns the current value of serial instance, then increments it"""
    def generate(self):
        curr_value = self.current
        self.current += 1
        return curr_value

    """resets back to the initially passed in value, and then returns it"""
    def reset(self):
        self.current = self.original
        #return self.original


class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # (a+ib) + (c+id) = ((a+c) + i(b+d))
    def add(self, complex):
        self.real += complex.real
        self.imag += complex.imag
    
    # (a+ib) + (c+id) = ((a-c) + i(b-d))
    def subtract(self, complex):
        self.real -= complex.real
        self.imag -= complex.imag

    # (a+ib)(c+id) = (ac-bd) + i(ad + cb)
    def multiply(self, complex):
        self.real = (self.real * complex.real) - (self.imag * complex.imag)
        self.imag = (self.real * complex.imag) + (complex.real * self.imag)
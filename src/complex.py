from math import sqrt, pow

class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # (a+ib) + (c+id) = ((a+c) + i(b+d))
    def add(self, complex):
        self.real += complex.real
        self.imag += complex.imag
    
    def add2(self, complex):
        return Complex(self.real + complex.real, self.imag + complex.imag)

    # (a+ib) + (c+id) = ((a-c) + i(b-d))
    def subtract(self, complex):
        self.real -= complex.real
        self.imag -= complex.imag

    def subtract2(self, complex):
        return Complex(self.real - complex.real, self.imag - complex.imag)

    # (a+ib)(c+id) = (ac-bd) + i(ad + cb)
    def multiply(self, complex):
        self.real = (self.real * complex.real) - (self.imag * complex.imag)
        self.imag = (self.real * complex.imag) + (complex.real * self.imag)

    def multiply2(self,complex):
        return Complex((self.real * complex.real) - (self.imag * complex.imag), (self.real * complex.imag) + (complex.real * self.imag))

    def getReal(self):
        return self.real

    def getImaginary(self):
        return self.imag

    def getMagnitude(self):
        return sqrt(pow(self.real, 2) + pow(self.imag, 2))

    # (1+2i)^-1 = 1/(1+2i)
    def getInverse(self):
        denominator = pow(self.real, 2) + pow(self.imag, 2)

        self.real /= denominator
        self.imag *= -1
        self.imag /=denominator

    def getInverse2(self):
        denominator = pow(self.real, 2) + pow(self.imag, 2)
        
        #return Complex(self.real/denominator, -1*self.imag/denominator)
        return Complex(self.real, -1*self.imag)

    def complexSquare(self):    
            temp = self.real
            self.real = pow(self.real, 2) + pow(self.imag, 2)
            self.imag = 2*temp*self.imag

    def toString(self):
        if(self.imag < 0):
            if -1*self.imag < 0.000001:
                return str(self.real)
            else:
                return str(self.real) + " - i" + str(self.imag*-1)
        elif(self.imag is 0):
            return str(self.real)
        elif(self.imag < 0.000001):
            return str(self.real)
        elif(self.real < 0.000001):
            if(self.imag < 0):
                return "-i" + str(self.imag*-1)
            else:
                return "i" + str(self.imag)
        else:
            return str(self.real) + " + i" + str(self.imag)
            
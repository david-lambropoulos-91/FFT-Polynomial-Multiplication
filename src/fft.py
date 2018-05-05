from complex import Complex
from math import cos, sin, pi, pow
from linecache import checkcache, getline
from sys import exc_info
from inspect import stack
from traceback import print_stack

class fft(object):
    def __init__(self):
        self.assignments = 0
        self.comparisons = 0
        self.exchanges = 0

    def printException(self, printStack=False):
        # Returns thread and current frame stack specifc information. 
        # (Exception type, Exception parameter, Traceback object)
        exceptionType, exceptionObject, traceBack = exc_info()

        # Get frame object at this level
        frame = traceBack.tb_frame

        # Get name of caller function
        function = stack()[1][3]

        # Get current line number in Python source code
        lineno = traceBack.tb_lineno

        # Get name of the file where error occurred via code object via the frame object
        filename = frame.f_code.co_filename

        # Get line lineno from file named filename. On error returns ''
        checkcache(filename)
        line = getline(filename, lineno, frame.f_globals)

        # Get name of the exception type
        exceptionName = exceptionType.__name__
        
        # Display error message
        print('[{}: {}] caused by "{}", at line {} in function {} in file {}'.format(exceptionName, exceptionObject, line.strip(), lineno, function, filename))
        

    # Create array of Roots of unity
    def getRootOfUnity(self, size):
        roots = []
        i = 0

        while i < size:

            roots.append(Complex(cos(2*i*pi/size), sin(2*i*pi/size)))

            i += 1

        return roots

    # Create array of inverse Roots of unity
    def getInverseRootsOfUnity(self, size):
        roots = []
        i = 0

        while i < size:
            roots.append(Complex(cos(2*i*pi/size), -1*sin(2*i*pi/size)))

            i += 1

        return roots

    # Convert polynomial (list of coefficients) to list of Complex objects 
    def convertPolynomial(self, polynomial, newSize):
        newPoly = []

        i = 0

        try:    
            for coefficient in polynomial:
                newPoly.append(Complex(coefficient, 0))
                i += 1

            while i < newSize:
                newPoly.append(Complex(0, 0))

                i += 1
        except:
            self.printException()
            exit(1)

        return newPoly 

    def fastFourierTransform(self, polynomial, newSize):
        tempSize = newSize
        temp = 2

        while tempSize > temp:
            temp *= 2
        
        tempSize = temp

        newPolynomial = self.convertPolynomial(polynomial, tempSize)
        
        return self.__fastFourierTransform(len(newPolynomial), newPolynomial, self.getRootOfUnity(len(newPolynomial)), 1)

    def __fastFourierTransform(self, size, polynomial, rootsOfUnity, power):
        if size is 1:
            return polynomial
        else:
            evenCoefficients = []
            oddCoefficients = []

            # Build even and odd lists of coefficients
            # O(m)
            for i in range(0, size):
                if i%2 is 0:
                    self.assignments += 1
                    evenCoefficients.append(polynomial[i])
                else:
                    self.assignments += 1
                    oddCoefficients.append(polynomial[i])

            # Do FFT of each half
            FEven = self.__fastFourierTransform(int(size/2), evenCoefficients, rootsOfUnity, power*2)
            FOdd = self.__fastFourierTransform(int(size/2), oddCoefficients, rootsOfUnity, power*2)
        
            try:
                F = []
                for i in range(0, size):
                    F.append(Complex(0,0))
                
                j = 0

                while j < size/2:
                    self.comparisons += 1

                    temp = rootsOfUnity[j*power].multiply2(FOdd[j]) 
                    F[j] = FEven[j].add2(temp)
                    F[j+int(size/2)] = FEven[j].subtract2(temp)
                    self.assignments += 3

                    j += 1
            except:
                self.printException()
                exit(1)
        return F

    def inverseFastFourierTransform(self, polynomial):
        size = len(polynomial)
        
        return self.__fastFourierTransform(size, polynomial, self.getInverseRootsOfUnity(size), 1)

    def getStatistics(self):
        return [self.assignments, self.comparisons, self.exchanges]
from complex import Complex
from math import cos, sin, pi, pow
from linecache import checkcache, getline
from sys import exc_info
from inspect import stack
from traceback import print_stack

class fft(object):
    def __init__(self):
        self.x = 0

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
        

    def getRootOfUnity(self, size):
        return Complex(cos(2*pi/size), sin(2*pi/size))

    def convertPolynomial(self, polynomial, newSize):
        newPoly = []

        i = 0
        try:    
            for coefficient in polynomial:
                newPoly.append(Complex(coefficient, 0))
                i += 1

            while i <= newSize:
                newPoly.append(Complex(0, 0))

                i += 1
        except:
            self.printException()
            exit(1)

        return newPoly 

    def fastFourierTransform(self, polynomial, newSize):
        size = len(polynomial)

        newPolynomial = self.convertPolynomial(polynomial, newSize)

        # for element in newPolynomial:
        #     print(element.toString())

        # exit(1)

        return self.__fastFourierTransform(len(newPolynomial), newPolynomial, self.getRootOfUnity(len(newPolynomial)))

    def __fastFourierTransform(self, size, polynomial, rootOfUnity):
        print("size = " + str(size))
        print("w = " + rootOfUnity.toString())

        if size is 1:
            return polynomial
        else:
            evenCoefficients = []
            oddCoefficients = []

            # Build even and odd lists of coefficients
            # O(m)
            for i in range(0, size):
                if i%2 is 0:
                    evenCoefficients.append(polynomial[i])
                else:
                    oddCoefficients.append(polynomial[i])

            # print("polynomial: " + str(polynomial))
            # print("even: " + str(evenCoefficients))
            # print("odd: " + str(oddCoefficients))
            # print("root of unity: " + rootOfUnity.toString())

            # rootOfUnity.complexSquare()           

            FEven = self.__fastFourierTransform(int(size/2), evenCoefficients, rootOfUnity.multiply2(rootOfUnity))
            FOdd = self.__fastFourierTransform(int(size/2), oddCoefficients, rootOfUnity.multiply2(rootOfUnity))
        
            try:
                F = []
                for i in range(0, size):
                    F.append(Complex(0,0))
                
                j = 0
                x = Complex(1,0)

                while j < size/2:
                    temp = x.multiply2(FOdd[j])
                    # print("temp = " + temp.toString())
                    F[j] = FEven[j].add2(temp)

                    temp = x.multiply2(FOdd[j])
                    F[j+int(size/2)] = FEven[j].subtract2(temp)
                
                    x.multiply(rootOfUnity)
                    j += 1
            except:
                self.printException()
                exit(1)
        return F

    def inverseFastFourierTransform(self, polynomial):
        size = len(polynomial)

        return self.__fastFourierTransform(size, polynomial, self.getRootOfUnity(size).getInverse2())
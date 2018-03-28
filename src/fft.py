from complex import Complex
from math import cos, sin, pi, pow

class fft(object):
    def __init__(self):
        self.x = 0

    def getRootOfUnity(self, size):
        return Complex(cos(2*pi/size), sin(2*pi/size))

    def fastFourierTransform(self, polynomial):
        size = len(polynomial)

        return self.__fastFourierTransform(size, polynomial, self.getRootOfUnity(size))

    def __fastFourierTransform(self, size, polynomial, rootOfUnity):
        print("size = " + str(size))
        if size is 1:
            print(polynomial)
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

            print("polynomial: " + str(polynomial))
            print("even: " + str(evenCoefficients))
            print("odd: " + str(oddCoefficients))
            # print("root of unity: " + rootOfUnity.toString())

            rootOfUnity.complexSquare()            

            FEven = self.__fastFourierTransform(int(size/2), evenCoefficients, rootOfUnity)
            FOdd = self.__fastFourierTransform(int(size/2), oddCoefficients, rootOfUnity)
        
            try:
                F = []
                for i in range(0, size):
                    F.append(Complex(0,0))
                
                j = 0
                x = Complex(1,0)

                while j < size/2:
                #     print("Here")
                    # print(F[j].toString())
                    c1 = Complex(FEven[j], 0)
                    print("c1 = " + c1.toString())
                    # F[j].add(c1)
                    # .add( x.multiply( Complex( FOdd[j], 0 ) ) ) )
                #     print("Here2")
                #     F[j+size/2].add(Complex(FEven[j], 0).subtract(x.multiply(Complex(FOdd[j], 0))))
                #     print("Here3")
                #     x.multiply(rootOfUnity)
                    j += 1
            except Exception as e:
                print(e)
        return F

    def inverseFastFourierTransform(self, polynomial):
        size = len(polynomial)

        return self.__fastFourierTransform(size, polynomial, self.getRootOfUnity(size).getInverse())
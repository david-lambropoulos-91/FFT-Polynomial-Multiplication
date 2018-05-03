from fft import fft

class polynomial(object):
    def __init__(self):
        self.assignments = 0
        self.comparisons = 0
        self.exchanges = 0 

    # A - array of m elements
    # B - array of n elements
    # Running Time: T(n) = O(nlogn) + O(nlogn) + O(n) + O(n) + O(nlogn) = O(nlogn)
    def fastMultiply(self, A, B):
        self.assignments = 0
        self.comparisons = 0
        self.exchanges = 0 
        
        FFT = fft()
        
        n = len(A)
        m = len(B)

        finalSize = n + m - 1
        
        try:
            FA = FFT.fastFourierTransform(A, finalSize)    # O(nlogn)
            
            FB = FFT.fastFourierTransform(B, finalSize)    # O(nlogn)
            FC = []
        except Exception as e:
            print(e)
            exit(0)

        try:
            # O(n)
            for i in range(0, len(FA)):
                FC.append(FA[i].multiply2(FB[i]))
            
            C = FFT.inverseFastFourierTransform(FC) # O(nlogn)

            # O(n)
            for element in C:
                element.multiply(1/(len(FA)))

        except Exception as e:
            FFT.printException()

        # Remove extra elements outside the size of the final array
        i = 0
        finalArray = []
        while i < finalSize:
            finalArray.append(C[i].getReal())
            
            i += 1

        return finalArray
        # print(C)

    # A - array of m elements
    # B - array of n elements
    def bruteForceMultiply(self, A, B):
        self.assignments = 0
        self.comparisons = 0
        self.exchanges = 0

        # Intialize C of size m+n-1
        C = []
        i = 0
        stop = len(A)+len(B)-1
        self.assignments += 3
        
        # O(m+n)
        while i < stop:
            C.append(0)
            i += 1
            self.comparisons += 1
            self.assignments += 2

        # O(n^2)
        i = 0
        self.assignments += 1
        for a in A:
            j = 0
            self.assignments += 1
            for b in B:
                C[i+j] += a*b
                j += 1
                self.comparisons += 1
                self.assignments += 2
            i += 1
            self.assignments += 1

        print(C)
        return C

    def printStatistics(self):
        print(self.assignments)
        print(self.comparisons)
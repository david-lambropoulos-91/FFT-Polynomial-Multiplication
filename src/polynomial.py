from fft import fft

class polynomial(object):
    def __init__(self):
        self.x = 0

    # A - array of m elements
    # B - array of n elements
    def fastMultiply(self, A, B):
        FFT = fft()
        
        n = len(A)
        m = len(B)

        finalSize = n + m - 1
        
        try:
            print("Starting A")
            FA = FFT.fastFourierTransform(A, finalSize)    # O(nlogn)
            
            print("\nStarting B\n")
            FB = FFT.fastFourierTransform(B, finalSize)    # O(nlogn)
            FC = []
        except Exception as e:
            print(e)
            exit(0)

        try:
            print("\nSTARTING FC\n")
            # O(n)
            for i in range(0, len(FA)):
                FC.append(FA[i].multiply2(FB[i]))
            C = FFT.inverseFastFourierTransform(FC)

            for element in C:
                element.multiply(1/len(A))


            print("ELEMENTS IN C")
            for element in C:
                print(element.toString())
        except Exception as e:
            FFT.printException()
        # print(C)

    # A - array of m elements
    # B - array of n elements
    def bruteForceMultiply(self, A, B):
        # Intialize C of size m+n-1
        C = []
        i = 0
        stop = len(A)+len(B)-1
        
        # O(m+n)
        while i < stop:
            C.append(0)
            i += 1

        # O(n^2)
        i = 0
        for a in A:
            j = 0
            for b in B:
                C[i+j] += a*b
                j += 1
            i += 1

        print(C)
        return C
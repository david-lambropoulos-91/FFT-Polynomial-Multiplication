from fft import fft

class polynomial(object):
    def __init__(self):
        self.x = 0

    # A - array of m elements
    # B - array of n elements
    def fastMultiply(self, A, B):
        FFT = fft()       
        try:
            FA = FFT.fastFourierTransform(A)    # O(nlogn)
            FB = FFT.fastFourierTransform(B)    # O(nlogn)
            FC = []
        except Exception as e:
            print(e)
            exit(0)

        print(FA)

        # O(n)
        # for i in range(0, len(A)):
        #     FC.append(FA[i].multiply(FB[i]))

        # C = 1/len(A) * FFT.inverseFastFourierTransform(FC)
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
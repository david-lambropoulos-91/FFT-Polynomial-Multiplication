class polynomial(object):
    def __init__(self):
        self.x = 0

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
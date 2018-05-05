from fft import fft

class polynomial(object):
    def __init__(self):
        self.assignments = 0
        self.comparisons = 0
        self.exchanges = 0 
        self.polynomial1 = []
        self.polynomial2 = []

    def readFile(self, filename1, filename2):
        # Read file from the user by going through line by line 
        # and extracting the numbers.
        print("Beginning to read data/" + filename1 + "...")
        try:
            with open("../data/"+filename1, "r") as file:
                for line in file:
                    self.polynomial1.append(int(line.rstrip()))
    
        except (OSError, IOError) as e:
            print("Could not read file! :(")
            print(e)
            exit(1)

        # Read file from the user by going through line by line 
        # and extracting the numbers.
        print("Beginning to read data/" + filename2 + "...")
        try:
            with open("../data/"+filename2, "r") as file:
                for line in file:
                    self.polynomial2.append(int(line.rstrip()))
    
        except (OSError, IOError) as e:
            print("Could not read file! :(")
            print(e)
            exit(1)

    # A - array of m elements
    # B - array of n elements
    # Running Time: T(n) = O(nlogn) + O(nlogn) + O(n) + O(n) + O(nlogn) = O(nlogn)
    def fastMultiply(self, A, B):
        self.assignments = 0
        self.comparisons = 0
        self.exchanges = 0 
        
        self.readFile(A, B)

        FFT = fft()
        
        n = len(self.polynomial1)
        m = len(self.polynomial2)

        finalSize = n + m - 1
        
        try:
            FA = FFT.fastFourierTransform(self.polynomial1, finalSize)    # O(nlogn)
            
            FB = FFT.fastFourierTransform(self.polynomial2, finalSize)    # O(nlogn)
            FC = []
        except Exception as e:
            print(e)
            exit(0)

        try:
            # O(n)
            for i in range(0, len(FA)):
                self.assignments += 1
                FC.append(FA[i].multiply2(FB[i]))
            
            C = FFT.inverseFastFourierTransform(FC) # O(nlogn)

            stats = FFT.getStatistics()

            self.assignments += stats[0]
            self.comparisons += stats[1]
            self.exchanges += stats[2]

            # O(n)
            for element in C:
                self.assignments += 1
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

        self.readFile(A,B)

        # Intialize C of size m+n-1
        C = []
        i = 0
        stop = len(self.polynomial1)+len(self.polynomial2)-1
        
        # O(m+n)
        while i < stop:
            C.append(0)
            i += 1

        # O(n^2)
        i = 0
        
        for a in self.polynomial1:
            j = 0
            self.assignments += 1
            for b in self.polynomial2:
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
from time import time, ctime, sleep
from sys import exit, argv
from polynomial import polynomial

def main(argc, argv):
    print(ctime())
    
    # Start timer
    start_time = time()

    # Start main program
    poly = polynomial()

    print("Using Brute Force")
    poly.bruteForceMultiply("8192coefficients.txt","8192coefficients.txt")
    poly.printStatistics()
    print("\nUsing FFT")

    try:
        print(poly.fastMultiply("8192coefficients.txt","8192coefficients.txt"))
        poly.printStatistics()
    except Exception as e:
        print(e)

    # Display execution time
    print("\n--- %s seconds ---\n" % (time() - start_time))

if __name__ == "__main__":
    try:
        main(len(argv), argv)
    except:
        exit(1)

    # Executed successfully
    exit(0)
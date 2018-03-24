from time import time, ctime, sleep
from sys import exit, argv

def main(argc, argv):
    while(1):
        print(ctime())
        
        # Start timer
        start_time = time()

        # Start main program

        # Display execution time
        print("\n--- %s seconds ---\n" % (time() - start_time))

        sleep(3600)

if __name__ == "__main__":
    try:
        main(len(argv), argv)
    except:
        exit(1)

    # Executed successfully
    exit(0)
from sys import exit, argv
from random import randint
from math import pow

import os

def main(argc, argv):
    if not os.path.exists("../data"):
        os.makedirs("../data")

    try:
        i = 0
        while i < 14:
            number = int(pow(2,i))

            with open("../data/"+str(number)+"coefficients.txt", "w+") as file:
                j = 0

                while(j < number):
                    file.write(str(randint(1,9000))+"\n")
                    j += 1

            i += 1


                
    except (OSError, IOError) as e:
        print("Could not create file! :(")
        print(e) 
        exit(1) 

if __name__ == "__main__":
    try:
        main(len(argv), argv)
    except Exception as e:
        print(e)
        exit(1)

    # Executed successfully
    exit(0)
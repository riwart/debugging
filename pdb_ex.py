import sys
from random import choice

random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    print("To exit this game type 'exit'")
    n1 = int(choice(random1))
    n2 = int(choice(random2))
    answer = input("what is {} times {}? ".format(n2, n1))

    # exit
    if answer == "exit":
        print("Now exiting game!")
        sys.exit()

    # determine if number is correct
    elif answer == n1 * n2:
        print("Correct!")
    else:
        print("Wrong!")

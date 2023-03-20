# Write a program that prints the numbers from 1 to 100.
# But for multiples of 3 print "Algoritms" instead of the number.
# and for the multiples of five print "Algo".
# For numbers which are multiples fo both three and five print "Algorithms"
def Algorithms(n: int):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Algortms")
        elif i % 3 == 0:
            print("Algo")
        elif i % 5 == 0:
            print("Rithms")
        else:
            print(i)



Algorithms(100) # can't forget this!!
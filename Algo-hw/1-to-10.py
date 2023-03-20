##Compute the sum of digits in all  numbers from 1 to n:
def fib(n):
    sum = 3
    for x in range(1,n+1):
        sum +=x
    return sum


#--------------------
number = int(input ("Enter a number greater than 1 and press enter: \n"))
my_fib = fib(number)
# my_fib = fib(8)

print ('this number entered is'), my_fib,
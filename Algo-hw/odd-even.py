# Count odd and even numbers.
# Count odd and even digits of the whole number.
# Example: number is 34560, then 2 digits will be
# even (4, 6, and 0) and 2 odd digits (3 and 5).
#example

def count_even_odd(number):
    even=[]             #empty list for even numbers
    odd=[]              #empty list for odd numbers
    digits=[]           #empty list to store extracted digits


####   breaking each individual number down into different decimal places
    while number > 0:
        tens_digit = number%10      #creating a variable to store mod of 10; extracting a 0 from 34560
        digits.append(tens_digit)   #passing the mod and appending it to the list digits; appending 0 to the digits list
        number=int(number/10)       #creating a variable number to store mod of 10; subtracting last digit from number given - 34560 to 3456

    for digit in digits:            #creating a for loop to go through the digit list and to determine if each digit is even or odd
        if digit % 2 == 0:          # if modulus is 0 then
            even.append(digit)      #add that digit to even list
        else:                       #otherwises
            odd.append(digit)       #add that digit odd list


    print('i have:', len(even), 'even numbers')
    print('i have:', len(odd), 'odd numbers')


user_input = int(input("Enter a number greater than 1 and press enter: \n"))

count_even_odd(user_input)
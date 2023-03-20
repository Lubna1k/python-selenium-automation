# Find the max number from 3 values.
# Example: 144, 21, 32. Result = 144.

def find_max(x,y,z):
    print (x, y, z)
    max = x
    if max<y:
        max= y

    if max<z:
        max = z

    return max

#------------#

my_max = find_max(14,698,91)
print(my_max)
# collatz conjecture revision

# the number we perform the collatz operations on
n = 25

# keep looping until we reach 1
while n != 1:
    print(n) # print the current value of n
    if n % 2 == 0: # checks if n is even
        n = n / 2 # if so divide by 2, single / gives decimals, double // gives a whole number or integer
    else: # if n is odd multiply by 3 and add 1
        n = (3 * n) + 1
# finally print the final value of n whch is always 1
print (n)




def gcd(a,b):
    while b!=0:
        # Continue updating a and b
        a, b = b, a % b
        # Return the GCD once the loop finishes
    return a

result=gcd(66528,52920)
print(result)
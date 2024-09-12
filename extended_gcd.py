
def extended_gcd(a, b):
    # Base case: when b becomes 0, the GCD is a, and the coefficients are u = 1, v = 0
    # This means that gcd(a, 0) = a, and a * 1 + 0 * v = a
    if b==0:
        return a , 1, 0 # Return GCD (a), and coefficients u = 1, v = 0
    else:
      # Recursive case: call extended_gcd with (b, a % b)
        gcd, u, v= extended_gcd(b, a%b)

    # Update u and v for the current recursion level
    # The new u is the old v, and the new v is calculated from the previous u and v
    # u = v (from the recursive step)
    # v = u - (a // b) * v
    u, v = v, u -(a//b)*v

    return gcd, u, v

p=26513
q=32321

# Call the extended_gcd function with p and q to get the GCD and coefficients u, v
gcd, u, v = extended_gcd(p, q)

# Print the GCD (which should be 1 because p and q are primes)
print(f"gcd{p}, {q} = {gcd}")

# print the values of u and v such that p * u + q * v = gcd(p, q)
print(f"u={u}, v={v}")
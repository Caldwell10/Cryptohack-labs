# Modulus
p = 29
# List of integers to check
ints = [14, 6, 11]

# Function to check if a number is a quadratic residue
def find_quadratic_residue(p, nums):
    for x in nums:
        for a in range(1, p):
            if (a * a) % p == x:
                print(f"{x} is a quadratic residue, and its square root is {a} (or {p - a})")
                return a  # Return the smaller root
        print(f"{x} is not a quadratic residue.")

# Running the function to find the quadratic residue and its square root
find_quadratic_residue(p, ints)

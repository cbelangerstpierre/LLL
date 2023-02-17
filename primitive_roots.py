import math
import timeit
import numpy
import sympy

# This function is used to perform a number of tests to determine if a number is a primitive root modulo `mod`.
def onlyTest(mod):
    # Calculate `mod - 1` and store the result in `mod_minus1` to not repeatedly make the operation
    mod_minus1 = mod - 1
    # Use `sympy.primefactors` to get the prime factors of `mod_minus1`, then map the function `mod_minus1 // x` (Integer division) over the list of prime factors to get our tests.
    tests = list(map(lambda x: mod_minus1 // x, sympy.primefactors(mod_minus1)))
    # Return a list of all numbers `a` between 1 and `mod - 1` inclusive, where `a` is not a perfect square and does not equal `1` when raised to the power of each test in `tests` modulo `mod`.
    return [a for a in range(1, mod) if math.isqrt(a) ** 2 != a and all(pow(a, test, mod) != 1 for test in tests)]

# This function performs the same tests as `onlyTest` in order to find the first primitive root and generates a list of `m` values for each other primitive roots.
def testAndMGenerate(mod):
    # Calculate `mod - 1` and store the result in `mod_minus1` to not repeatedly make the operation
    mod_minus1 = mod - 1
    # Use `sympy.primefactors` to get the prime factors of `mod_minus1`, then map the function `mod_minus1 // x` (Integer division) over the list of prime factors to get our tests.
    tests = list(map(lambda x: mod_minus1 // x, sympy.primefactors(mod_minus1)))
    # Loop over all numbers `a` between 1 and `mod - 1` inclusive.
    for a in range(1, mod):
        # If `a` is not a perfect square and does not equal `1` when raised to the power of each test in `tests` modulo `mod`, return a sorted list of `m` values, where each `m` is calculated as `pow(a, m, mod)`, with `m` ranging from 1 to `mod - 1` inclusive and `math.gcd(m, mod_minus1) == 1` to get every primitive roots.
        if math.isqrt(a) ** 2 != a and all(pow(a, test, mod) != 1 for test in tests):
            return sorted([pow(a, m, mod) for m in range(1, mod) if math.gcd(m, mod_minus1) == 1])


def primesfrom2to(n):
    # Create a NumPy array of ones with a length of n // 3 + (n % 6 == 2)
    # The data type of the array is set to boolean
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=bool)
    
    # Loop through the range from 1 to int(n ** 0.5) // 3 + 1
    for i in range(1, int(n ** 0.5) // 3 + 1):
        # If the value at index i of the sieve array is True
        if sieve[i]:
            # Calculate k as 3 * i + 1 with a bitwise OR with 1
            k = 3 * i + 1 | 1
            # Set every 2k-th value in the sieve array starting from k * k // 3 to False
            sieve[k * k // 3::2 * k] = False
            # Set every 2k-th value in the sieve array starting from k * (k - 2 * (i & 1) + 4) // 3 to False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    
    # Return a concatenated array of 2, 3, and the result of adding 1 to every value in the sieve array
    # that is the result of 3 * the non-zero values in the sieve array starting from the second value
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]

def test_function(function):
    # Record the start time
    start = timeit.default_timer()
    
    # Loop through the list of prime numbers up to a certain number
    for q in list(map(int, primesfrom2to(200))):
        # Call the function argument and pass the prime number as an argument
        result = function(q)
        print(q, "->", result) # Code to add to see the results
    
    # Print the time it took to run the function on all prime numbers
    print("Time :", timeit.default_timer() - start)

# Call the test_function with onlyTest as the argument
# test_function(onlyTest)
# Call the test_function with testAndMGenerate as the argument
test_function(testAndMGenerate)

import timeit
import sympy


def get_vector_generator(q, gen):
    vector_generator = []
    inverse = pow(gen, -1, q)
    list_of_primes = []

    for f in range (2,q-1):
        if sympy.ntheory.isprime(f) == True:
            list_of_primes.append(f) 
            
    # start = timeit.default_timer()
    for b in range (1, q):
        if b in list_of_primes :
            counter=0
            while b % q != 1:
                counter += 1
                b = b * inverse
            vector_generator.append(counter)
            

    return vector_generator
    # print("Time:", timeit.default_timer() - start)
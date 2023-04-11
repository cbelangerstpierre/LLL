import math
import timeit
import numpy
import sympy
from primitive_roots import primesfrom2to


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

def get_vector_generator2(q, gen):
    vector_generator = []
    inverse = pow(gen, -1, q)
    list_of_primes = []

    i = 2
    count = math.floor(math.log(q))
    while len(list_of_primes) != count:
        if sympy.ntheory.isprime(i) == True:
            list_of_primes.append(i)
        i += 1
            
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
    
    
    

def get_vector_generator3(q, gen):
    list_of_primes = []
    
    for f in range (2,q-1):
        if sympy.isprime(f):
            list_of_primes.append(f)
        if len(list_of_primes) == math.floor(math.log(q)):
            break
    list_of_primes2 = list_of_primes.copy()
    
    for exp in range(1, q):
        a = pow(gen, exp, q)
        if a in list_of_primes:
            index_exp = list_of_primes.index(a)
            list_of_primes2[index_exp] = exp
    return list_of_primes2



# print(get_vector_generator(101, 2))
# print(get_vector_generator2(101, 2))

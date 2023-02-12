# The LLL function takes in a list of vectors and a value for the reduction parameter delta
def LLL(vectors, delta):
    # A function to calculate the inner product of two vectors
    def innerProduct(vector1, vector2):
        return sum([vector1[pos] * vector2[pos] for pos in range(len(vector1))])
    
    # A function to calculate the difference between two vectors
    def difference(vector1, vector2):
        return [vector1[pos] - vector2[pos] for pos in range(len(vector1))]
    
    # A function to calculate the summation of vectors
    def summations(vectors_):
        return [sum([vector[pos] for vector in vectors_]) for pos in range(len(vectors_[0]))]
    
    # A function to multiply a vector by a scalar
    def multiplication(vector, amount):
        return [vector[pos] * amount for pos in range(len(vector))]
    
    # A function to determine if two vectors meet the Lovasz condition
    def lovasz(reduced1, reduced2, base2):
        return innerProduct(reduced2, reduced2) >= (
                delta - (innerProduct(base2, reduced1) / innerProduct(reduced1, reduced1)) ** 2) * innerProduct(
            reduced1, reduced1)
    
    # A function to perform the Gram-Schmidt orthogonalization
    def gramSchimdt(B, Bstar, pos):
        vectorsTemp = []
        # Calculate the projections of the new vector onto all previous orthogonal vectors
        for incrementer in range(pos):
            vectorsTemp.append(multiplication(Bstar[incrementer],
                                              innerProduct(B[pos], Bstar[incrementer]) / innerProduct(
                                                  Bstar[incrementer], Bstar[incrementer])))
        # Calculate the orthogonal vector
        finalStar = difference(B[pos], summations(vectorsTemp))
        final = B[pos]
        # Project the new vector onto all previous orthogonal vectors
        for incrementer in range(pos):
            final = difference(final, multiplication(B[incrementer], round(
                innerProduct(final, Bstar[incrementer]) / innerProduct(Bstar[incrementer], Bstar[incrementer]))))
        return final, finalStar
    
    # Initialize the iteration counter
    i = 1
    
    # Repeat the loop until all vectors have been processed
    while i < len(vectors):
        # Copy the original vectors
        reduced_vectors = vectors.copy()
        # Iterate through all previous vectors
        for j in range(1, i + 1):
            # Perform the Gram-Schmidt orthogonalization on the current vector
            vectors[i], reduced_vectors[i] = gramSchimdt(vectors, reduced_vectors, i)

            # Check if the length of the new vector is too large and needs to be reduced
            if not lovasz(reduced_vectors[i - 1], reduced_vectors[i], vectors[i]):
                # Swap the current and previous vectors
                vectors[i - 1], vectors[i] = vectors[i], vectors[i - 1]
                
                # Decrement the counter so that the previous vector can be processed again
                i -= 1
                
        # Increment the counter to move to the next vector
        i += 1
        
    # Return the processed vectors
    return vectors


# Test the LLL function with two sets of vectors
print(LLL([[201, 37], [1648, 297]], 0.75))
print(LLL([[15, 23, 11], [46, 15, 3], [32, 1, 1]], 0.75))

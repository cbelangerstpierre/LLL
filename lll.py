def LLL(vectors, delta):
    def innerProduct(vector1, vector2):
        return sum([vector1[pos] * vector2[pos] for pos in range(len(vector1))])

    def difference(vector1, vector2):
        return [vector1[pos] - vector2[pos] for pos in range(len(vector1))]

    def summations(vectors_):
        return [sum([vector[pos] for vector in vectors_]) for pos in range(len(vectors_[0]))]

    def multiplication(vector, amount):
        return [vector[pos] * amount for pos in range(len(vector))]

    def lovasz(reduced1, reduced2, base2):
        return innerProduct(reduced2, reduced2) >= (
                delta - (innerProduct(base2, reduced1) / innerProduct(reduced1, reduced1)) ** 2) * innerProduct(
            reduced1, reduced1)

    def gramSchimdt(B, Bstar, pos):
        vectorsTemp = []
        for incrementer in range(pos):
            vectorsTemp.append(multiplication(Bstar[incrementer],
                                              innerProduct(B[pos], Bstar[incrementer]) / innerProduct(
                                                  Bstar[incrementer], Bstar[incrementer])))

        finalStar = difference(B[pos], summations(vectorsTemp))
        final = B[pos]
        for incrementer in range(pos):
            final = difference(final, multiplication(B[incrementer], round(
                innerProduct(final, Bstar[incrementer]) / innerProduct(Bstar[incrementer], Bstar[incrementer]))))
        return final, finalStar

    i = 1

    while i < len(vectors):
        reduced_vectors = vectors.copy()
        for j in range(1, i + 1):
            vectors[i], reduced_vectors[i] = gramSchimdt(vectors, reduced_vectors, i)

            if not lovasz(reduced_vectors[i - 1], reduced_vectors[i], vectors[i]):
                vectors[i - 1], vectors[i] = vectors[i], vectors[i - 1]
                i -= 1
        i += 1

    return vectors


print(LLL([[201, 37], [1648, 297]], 0.75))
print(LLL([[15, 23, 11], [46, 15, 3], [32, 1, 1]], 0.75))

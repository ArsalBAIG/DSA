def cubic_algo(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix[i][j][k] += 1
            print(matrix)

matrix = [[[3,4], [5,6], [4,5], [8,9]]]
cubic_algo(matrix)


# Here, algo do:
# It iterates 3 times so it's a cubic notation.
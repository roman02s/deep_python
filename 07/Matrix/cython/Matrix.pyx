cpdef list matrix_mul(list matrix_1, list matrix_2):
    cpdef list result = []
    cpdef list res = []
    cpdef int el = 0
    cpdef int m = 0
    for i in range(len(matrix_1[0])):
        res = []
        for j in range(len(matrix_2)):
            el = 0
            m = 0
            for k in range(len(matrix_1)):
                m = matrix_1[i][k] * matrix_2[k][j]
                el += m
            res.append(el)
        result.append(res)
    return result

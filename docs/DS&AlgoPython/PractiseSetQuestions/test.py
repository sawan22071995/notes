def diagonal_sum(matrix):
    # TODO
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i] == matrix[j]:
                sum += matrix[i][j]
    return sum

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
print(diagonal_sum(myList2D)) # 15                
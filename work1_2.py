'''
นายธนธัชย์ ชัยพุทธา 6440201561
'''
#Number 1
matrix = []

def array_1():
    for i in range(3):
        n = []
        for j in range(4):
            data = float(input(f"Enter number row {i+1} column {j+1}: "))
            n.append(data)
        matrix.append(n)

def total_number():
    total = 0
    for i in matrix:
        for j in i:
            total += j
    return total

#Number 2
matrix_1 = []
matrix_2 = []

def matrix1():
    for c in range(1, 3, 1):
        for i in range(3):
            n = [] 
            for j in range(3):
                data = float(input(f"Enter number matrix {c} row {i+1} column {j+1}: "))
                n.append(data)
            if c == 1:     
                matrix_1.append(n)
            elif c == 2:
                matrix_2.append(n)

def total_number1():
    total_matrix_1 = 0
    total_matrix_2 = 0
    for i in matrix_1:
        for j in i:
            total_matrix_1 += j
    for i2 in matrix_2:
        for j2 in i2:
            total_matrix_2 += j2
    result = total_matrix_1 + total_matrix_2
    return result

#Number 3
matrix_3 = []
matrix_4 = []

def matrix2():
    for c in range(1,3,1):
        for i in range(3):
            n = []
            for j in range(3):
                data = float(input(f"Enter number matrix {c} row {i+1} column {j+1}: "))
                n.append(data)
            if c == 1:
                matrix_3.append(n)
            elif c == 2:
                matrix_4.append(n)

def total_number2():
    total_matrix_1 = 1
    total_matrix_2 = 1
    for i in range(len(matrix_3)):
        for j in range(len(matrix_3[i])):
            total_matrix_1 *= matrix_3[i][j]
    for i2 in matrix_4:
        for j2 in i2:
            total_matrix_2 *= j2
    result = total_matrix_1 * total_matrix_2
    return result

if __name__ == "__main__":
    array_1()
    total = total_number()
    #matrix1()
    #total1 = total_number1()
    #matrix2()
    #total2 = total_number2()
    print(f"Positive result: {total}")

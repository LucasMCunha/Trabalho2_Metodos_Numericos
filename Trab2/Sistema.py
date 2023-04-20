# def skipper():
#     if(A[i][j] == 0):
#         skipper+1 
#         if(skipper == 0 & guard == false):
#             guard = true
#             if(skipper != 0):
#                 return 0


def gauss(A):
    for i in range(len(A) - 1):
       for j in range(i + 1,len(A)):
           aux1 = A[j][i]
           if aux1 == 0:
               for k in range(i,len(A)):
                   if A[k][i] != 0:
                       swap(A, i, k)
                       aux1 = A[j][i]
           aux2 = A[i][i]
           if aux2 == 0:
               continue
           div = aux1 / aux2
           A[j] = sumVector(multVector(A[i], -div), A[j])
    return A

def reader():
    size = 0
    entrance = []
    created = False
    with open('example.txt') as f:
       for line in f.readlines():
        data = line.split(" ")
        if(data[0] == "Entrada"):
            size += 1
            entrace = data[3]
        else:
            if (created == False):
                matrix = [size-1][size]
                created = True
                for i in len(entrace):
                    matrix [i][size] = entrance[i]
        a = ord(data[4]) - 65
        b = ord(data[0]) - 65
        matrix[a][b] = data[2]
    return matrix
                



def swap(A, i, j):
    newI = []
    newJ = []
    for index in range(len(A) + 1):
        newI += [A[j][index]]
        newJ += [A[i][index]]
    A[i] = newI
    A[j] = newJ

def multVector(v, x):
    newV = []
    for i in range(len(v)):
        newV += [v[i] * x]
    return newV

def sumVector(v1, v2):
    newV = []
    for i in range(len(v1)):
        newV += [v1[i] + v2[i]]
    return newV

def main():
    i =0
    A = reader()
    print(A)
    return 0



#def pivotamento(A):
#    for i in xrange(len(A) - 1):
#        for j in xrange(i + 1,len(A)):
#            n1 = A[j][i]
#            if n1 == 0:
#                for k in xrange(i,len(A)):
#                    if A[k][i] != 0:
#                        swap(A, i, k)
#                        n1 = A[j][i]
#            n2 = A[i][i]
#            if n2 == 0:
#                continue
#            div = n1 / n2
#            A[j] = sumVector(multVector(A[i], -div), A[j])
#    return A
#
#
#def multVector(v, x):
#    newV = []
#    for i in xrange(len(v)):
#        newV += [v[i] * x]
#    return newV
#
#def sumVector(v1, v2):
#    newV = []
#    for i in xrange(len(v1)):
#        newV += [v1[i] + v2[i]]
#    return newV
#
#def swap(A, i, j):
#    newI = []
#    newJ = []
#    for index in xrange(len(A) + 1):
#        newI += [A[j][index]]
#        newJ += [A[i][index]]
#    A[i] = newI
#    A[j] = newJ
#
#def printMatrix(A):
#    for i in A:
#        for j in i:
#             print (A[i][j])
#
#A = [[1.0, -1.0, 2.0, -1.0, -8.0], [2.0, -2.0, 3.0, -3.0, -20], [1.0, 1.0, 1.0, 0.0, -2.0], [1.0, -1.0, 4.0, -3.0, 4.0]]
#printMatrix(A)
#print("\n\n")
#printMatrix(pivotamento(A))
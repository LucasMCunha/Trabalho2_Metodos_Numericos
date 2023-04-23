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

def gaussSolver(A):
    size = len(A)
    aux = 0
    x =[]
    for i in range(size):
        x.append(1)
    for i in range(1,size+1):
      a = 0
      for j in range(size):
        if (j>(size-i)):
         aux = aux+1
         a = a + (x[j] * A[size-i][j])
      x[size-i] = (A[size-i][size] - a)/A[size-i][size-i]
    print(aux)
    return x

def reader():
    size = 0
    entrance = []
    created = False
    with open('casoa.txt') as f:
       for line in f.readlines():
        data = line.split(" ")
        if(data[0] == "Entrada"):
            size += 1
            entrance.append(float(data[3]))
        else:
            if (created == False):
                matrix = [[0 for x in range(size+1)] for y in range(size)]
                created = True
                for i in range(size):
                    matrix [i][size] = entrance[i] * -1
            if(data[0] != "Entrada"):
                a1 = data[4].rstrip('\n')
                b = ord(a1) - 65
                a = ord(data[0]) - 65
                if (a == b):
                    matrix[a][b] = float(data[2]) -1
                else:
                    matrix[a][b] = float(data[2])
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

if __name__ == "__main__":
    A = reader()
    gauss(A)
    print(gaussSolver(A))
#    print(A)

#    if __name__ == "__main__":
#     main()
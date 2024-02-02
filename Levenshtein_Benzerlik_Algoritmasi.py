import numpy 

def minimum(a,b,c):
    if a<b and a<c:
        return a 
    elif b<a and b<c:
        return c
    elif c<a and c<b:
        return c
    
def max(a,b):
    if a<b :
        return b
    if b<a :
        return a
    
def normalize(X,size):
    if len(X) < size:
        fark =size - len(X)
        for i in range(fark):
            X = X + " "
    return X 
       
def LevenshteinMesafesi(A,B):
    len_A=len(A)
    len_B=len(B)
    silme=0
    ekleme=0
    yer_degistirme=0

    K=numpy.zeros((len_A+1,len_B+1))
    for i in range(len_A):
       K[i][0]=i
    for i in range(len_B):
        K[0][i]=i

    for i in range(1,len_A):
        for j in range(1,len_B):

            if A[i-1] == B[j-1]:
                K[i][j]=K[i-1][j-1]
            else :
                silme =  K[i-1][j]+1
                ekleme = K[i][j-1]+1
                yer_degistirme = K[i-1][j-1]+1
                K[i][j] = minimum(yer_degistirme,silme,ekleme)
    return K[i-1][j-1]             








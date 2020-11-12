from pandas import DataFrame

def lcs(X, Y): 
    m = len(X)
    n = len(Y)
    b = [[' ']*(n+1) for i in range(m+1)]
    c = [[' ']*(n+1) for i in range(m+1)]
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(1, m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '↖'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '↑'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '←'
    return b,c

def print_lcs_matrix(X, Y, b,c):
    m = len(X)
    n = len(Y)
    tempX = 'X' + X
    header = '\tY\t' + ''.join([f'{y}\t' for y in Y])
    print('-'*4*len(header))
    print(header)
    print('-'*4*len(header))
    for i in range(m+1):
        row = f' \t' + '\t'.join([str(x) for x in b[i]])
        row += f'\n{tempX[i]}\t' + '\t'.join([str(x) for x in c[i]])
        print(row)
        print('-'*4*len(header))

def print_lcs(b,X,i,j):
    if i==0 or j==0:
        return None
    
    if b[i][j] == '↖':
        print_lcs(b, X, i-1, j-1)
        print(X[i-1], end='')
    elif b[i][j] == '↑':
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)

if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    b, c =  lcs(X, Y)
    print_lcs_matrix(X, Y, b, c)
    print('\nMaior subsequencia comum: ', end='')
    print_lcs(b,X,len(b)-1,len(b[0])-1)
    print('\n')
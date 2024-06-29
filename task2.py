N = 3

def rotateMatrix(mat):
    for x in range(0, int(N / 2)):

        for y in range(x, N-x-1):
            temp = mat[x][y]
            mat[x][y] = mat[y][N-1-x]
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
            mat[N-1-y][x] = temp

def displayMatrix(mat):
 
    for i in range(0, N):
 
        for j in range(0, N):
 
            print(mat[i][j], end=' ')
        print("")
 
 
if __name__ == "__main__":
    mat = [[0 for x in range(N)] for y in range(N)]
 
    mat = [[1, 2, 4],
           [5, 6 ,8],
           [9,3,9]]
 
    rotateMatrix(mat)
 
    displayMatrix(mat)
 
 

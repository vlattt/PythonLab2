fm=[[1,2,3],[4,5,6],[7,8,9]]
sm=[[1,2,3],[4,5,6],[7,8,9]]
rm=[[0 for i in range(len(fm))] for i in range(len(fm))]
for i in range(len(fm)):
    for j in range(len(fm)):
        for k in range(len(fm)):
            rm=[[sum(fm[i][k] * sm[k][j] for k in range(len(fm))) for j in range(len(fm))] for i in range(len(fm))]
print(rm)

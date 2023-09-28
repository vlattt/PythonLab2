m=[[1,2],[4,5],[7,8]]
print(m)
mt=[[0 for j in range(len(m))] for i in range(len(m))]
print(mt)
for i in range(len(m)):
    for j in range(len(m[0])):
        mt[j][i]=m[i][j]
print(m)
print(mt)

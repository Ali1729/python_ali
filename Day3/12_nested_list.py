import copy
a = [[0,1,2],[3,4,5],[6,7,8]]
# b = a
b =copy.deepcopy(a)

for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] =  b[i][j]+1

print(b)

for i in range(len(b)):
    for j in range(len(b[i])):
        a[i][j] = b[i][j]-a[i][j]

print(a)
# a[0][0]-b[0][0]
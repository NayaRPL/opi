print("total matrix")
mat=[[1,4,5],
     [2,6,5]]
for baris in mat:
    print(baris)
total=1
for i in range (len(mat)):
   for j in range(len(mat[0])):
       total=total*mat[i][j]
print(total)

print("total list")
data=[2,7,8]
total=1
for i in range(len(data)):
    total=total*data[i]
print(total)
        
    
n=['n','j','f','t','s']
n[2]= ('k')
print(n)

#A矩阵输入
A=[]
print("请输入第一个矩阵的行数：")
rankA_row=int(input())
print("请输入第一个矩阵的列数：")
rankA_column=int(input())
print("请输入第一个矩阵：")
for i in range(0,rankA_row):
    temp=[]
    for j in range(0,rankA_column):
        n=int(input())
        temp.append(n)
    A.append(temp)
print(A)

#B矩阵输入
B=[]
print("请输入第二个矩阵的行数：")
rankB_row=int(input())
print("请输入第二个矩阵的列数：")
rankB_column=int(input())
print("请输入第二个矩阵：")
for i in range(0,rankB_row):
    temp=[]
    for j in range(0,rankB_column):
        n=int(input())
        temp.append(n)
    B.append(temp)
print(B)

#初始化
C=[]
for i in range(0,rankA_row):
    temp=[]
    for j in range(0,rankB_column):
        n=0
        temp.append(n)
    C.append(temp)
    tem=[]

#乘法运算
if rankA_column==rankB_row:
    
    for i in range(0,rankA_row):
        for j in range(0,rankB_column):
            for m in range(0,rankA_column):    
                C[i][j]+=A[i][m]*B[m][j]
    print(C)
else:
    print("error 两矩阵无法相乘！")



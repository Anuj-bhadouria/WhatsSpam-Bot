# m1=[[1,2],[3,4]]
# m2=[[4,5],[6,7]]
# res=[[0,0],[0,0]]

# for i in range(2):
#     for j in range(2):
#         res[i][j]=(m1[i][0]*m2[0][j]+
#                    m1[i][1]*m2[1][j])
        
# for i in res:
#     print(i)

# Input for Matrix A
print("Enter elements of Matrix A:")
a11 = int(input("A[1][1]: "))
a12 = int(input("A[1][2]: "))
a21 = int(input("A[2][1]: "))
a22 = int(input("A[2][2]: "))

# Input for Matrix B
print("Enter elements of Matrix B:")
b11 = int(input("B[1][1]: "))
b12 = int(input("B[1][2]: "))
b21 = int(input("B[2][1]: "))
b22 = int(input("B[2][2]: "))

# Multiply manually
c11 = a11*b11 + a12*b21
c12 = a11*b12 + a12*b22
c21 = a21*b11 + a22*b21
c22 = a21*b12 + a22*b22

# Print result
print("\nProduct of matrices:")
print([c11, c12])
print([c21, c22])

#defining the variables
A = 5
B = 8
C = 10
X = A + B + C
Y = C - B
Z = A*B*C
W = C / A
if A > B:
    print(A, "is greater than" ,B)
else:
    print(B, "is grater than " ,A)
    
print("sum of A,B,C is :",X)
print("Sub of C-B  is :",Y)
print("multiplication of A,B,C  is :",Z)
print("division of C/A is :",W)
arr = [1,4,6,3,74,35,23,76,45]
print (arr)

MAX = max(arr)
print ("laregest number in the array is :",MAX)

SMALL = min(arr)
print ("Smallest number in the array is :",SMALL)

for index, NUM in enumerate(arr):
    TOTAL += NUM
AVG = TOTAL/len(arr)
print ("Average:",AVG)

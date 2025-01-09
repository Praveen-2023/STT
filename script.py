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
print("sum of a,b,c  is :",X)
print("Sub of c-b  is :",Y)
print("multiplication of a,b,c  is :",Z)
print("division of c/a is :",W)
arr = [1,4,6,3,74,35,23,76,45]
print (arr)
MAX = 0
for i in range(0, len(arr)):
    if arr[i] > MAX:
        MAX = arr[i]
print ("laregest number in the array is :",MAX)
SMALL = arr[0]
for i in range(0, len(arr)):
    if arr[i] < SMALL:
        SMALL = arr[i]
print ("Smallest number in the array is :",SMALL)
TOTAL=0
for i in range(0, len(arr)):
    TOTAL += arr[i]
AVG = TOTAL/len(arr)
print ("Average:",AVG)

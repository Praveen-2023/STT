a = 5
b = 8
c = 10
add = a + b + c
sub = c - b
mult = a*b*c
divide = c / a
if a > b:
    print(a, "is greater than" ,b)
else:
    print(b, "is grater than " ,a)
print("sum of a,b,c  is :",add)
print("Sub of c-b  is :",sub)
print("multiplication of a,b,c  is :",mult)
print("division of c/a is :",divide)
arr = [1,4,6,3,74,35,23,76,45]
print (arr)
max = 0
for i in range(0, len(arr)):
    if arr[i] > max:
        max = arr[i]
print ("laregest number in the array is :",max)
small = arr[0]
for i in range(0, len(arr)):
    if arr[i] < small:
        small = arr[i]
print ("Smallest number in the array is :",small)
total =0
for i in range(0, len(arr)):
    total += arr[i]
average = total/len(arr)
print ("Average:",average)
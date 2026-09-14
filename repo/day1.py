# finding greater ot three numbers
print("Enter 3 numbers to compare..")
x = int(input("First Number.."))
y = int(input("Second Number.. ."))
z = int(input("Third Number..."))
if (x > y):
    if(x > z):
        print(x , "is the highest number")
    else:
        print(z , "is the highest number")
if(y > z):
    print(y , "is the highest value")
else:
    print(z , "is the highest value")
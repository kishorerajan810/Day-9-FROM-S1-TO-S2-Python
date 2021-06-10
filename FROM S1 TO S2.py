a=input("enter :").lower()
b=input("Enter :").lower()
x=int(input("enter :"))
y,z=list(a),list(b)
count=0
for i in a:
    for j in b:
        if(i==j):
            print(z.pop(j))
        count+=1
print(count)

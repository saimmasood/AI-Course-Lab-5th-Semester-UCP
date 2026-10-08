a=[1,3,5]
b=[2,4,6]

c=a+b

d=c.copy()
d.sort()

d.reverse()

c[3]=42

d.append(10)

c.append(7)
c.append(8)
c.append(9)

print("First 3 Elements of C:")
for i in range(0,3):
    print(c[i])

print("Last Element of D:",d[-1])

print("Length of D:",len(d))


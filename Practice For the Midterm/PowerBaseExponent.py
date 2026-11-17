

def findPower(b,e):

    if e==0:
        return 1

    x=b
    for i in range(1,e):
        b=b*x

    return b

b=int(input("Enter a base to get the power:"))
e=int(input("enter the exponent to get the power:"))

print("Power = ",findPower(b,e))



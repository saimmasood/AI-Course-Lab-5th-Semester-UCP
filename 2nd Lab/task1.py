numberList =[1,2,3,4,5,6,7,8]
sum=0
a=len(numberList)

for i in numberList:
        sum=sum+i

       
if a%2!=0:
    median=numberList[int((a/2)+1)]
else:
    centre=int(a/2)
    median=(numberList[centre]+numberList[centre-1])/2
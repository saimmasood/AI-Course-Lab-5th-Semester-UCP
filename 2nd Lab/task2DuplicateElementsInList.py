def dup(li):
    temp=[]
   
    for i in range(0,len(li)):
        for j in range(i+1,len(li)):
            if li[j]==li[i]:
                temp.append(li[j])
                break
               
    return temp
   
   
   
li=[1,2,3,5,6,1,3,6,5]

duplicateElements =dup(li)

for i in duplicateElements:
    print(i," ")
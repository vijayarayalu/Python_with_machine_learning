sentense=input("enter the sentense?\n").split(" ")
count=0
new_sentense=[]

for i in sentense: #the
    for j in range(1,len(i)+1): #1,2,3
        if len(i)%j==0:
            count+=1
    if count==2:
        new_sentense.append(i)
        count=0
    else:
        count=0
print("".join(new_sentense))
        
            
        
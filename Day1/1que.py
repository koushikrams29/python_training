
s="Hello world and Hello Earth"
x=list(s.split())
dic={}
for i in x:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

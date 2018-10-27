'''ceaser cipher encryption scheme using pythonv3
omkar gavhane'''
dict={}
res=""
list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text=input("enter text=")
op,k=input("E)ncrypt|D)ecrypt,key-").split(',')
for i in range(26):
	if op.lower()=="e": 
		dict[list[i]]=list[(i+int(k))%26]
	elif op.lower()=="d":
		dict[list[i]]=list[(i-int(k))%26]
for t in text:
	if t in list:
		res=res+dict[t]
	else:
		res=res+t
print(res)


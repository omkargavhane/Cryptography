'''transposition cipher scheme using python v3
omkar gavhane'''
from math import ceil
list=[] ; res=''
text=input("enter text-")
op,key=input("E)ncrypt|D)ecrypt,key-").split(',')
start=0 ; key=int(key)
if op.lower()=='d':
	key=ceil(len(text)/int(key))
for i in range(ceil(len(text)/key)):
	list.append(text[start:start+key])
	start+=key
list[-1]=list[-1]+((key-len(list[-1]))*' ')
for i in range(key):
	for j in range(len(list)):
		res=res+list[j][i]
print(res)

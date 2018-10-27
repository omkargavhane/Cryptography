plain_text=input("enter text here:")
op,key=input("e)ncrypt or d)ecrypt,key:").split(",")
plaintext_mat=[]
if op.lower()=="e":plain_text=plain_text+' '*(int(key)-len(plain_text)%int(key))
elif op.lower()=="d":key=int(len(plain_text)/int(key))
for i in range(0,len(plain_text),int(key)):plaintext_mat.append(list(plain_text[i:i+int(key)]))
zo=list(zip(*plaintext_mat))
for e in zo:print(''.join(e),end="")

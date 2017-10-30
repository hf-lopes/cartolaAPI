import threading
import time
def PrintThread():
    print(threading.current_thread().name)
    time.sleep(5)

for i in range(10):
    print('aqui')
    t = threading.Thread(name='t' + str(i),
                         target=PrintThread)
    t.start()
    print('ali')
    print('Thread %s Running' % t.name)
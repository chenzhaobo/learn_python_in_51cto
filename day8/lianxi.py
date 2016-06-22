import threading
import time
import random
def show1(num):
    for i  in range(5):
        print(num,'线程内执行',i)
        k = random.randint(1,5)
        print(num,'sleep',k)
        time.sleep(k)
therad_list = []
for t in range(5):
    t1 = threading.Thread(target=show1,args=[t,])
    therad_list.append(t1)
    t1.start()

print('before wait')
for x in therad_list:
    x.join()
print('after wait')
# for x in therad_list:
#     x.start()

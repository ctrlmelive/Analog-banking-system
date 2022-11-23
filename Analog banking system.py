from threading import Thread
from time import sleep

bank = {
    'byhy' : 0
}


def deposit(theadidx,amount):
    balance =  bank['byhy']

    sleep(0.1)
    bank['byhy']  = balance + amount
    print(f'subthread {theadidx} end')

theadlist = []
for idx in range(10):
    thread = Thread(target = deposit,
                    args = (idx,1)
                    )
    thread.start()
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('Main thread end')
print(f'Finally, our account balance is {bank["byhy"]}')
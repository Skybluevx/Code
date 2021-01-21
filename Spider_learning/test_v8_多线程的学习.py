import threading
import random
import time


gMoney = 1000
gLock = threading.Lock()
gTime = 0
gTotalTime = 10


class Product(threading.Thread):
    def run(self):
        global gMoney, gTotalTime, gTime
        while gTime <= gTotalTime:
            money = random.randint(100, 1000)
            gLock.acquire()
            gMoney += money
            gTime += 1
            print("{}生产了{}元钱，剩余{}元钱".format(threading.current_thread(), money,
                                            gMoney))
            gLock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney, gTime, gTotalTime
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print("{}消费者消费了{}元钱，剩余{}元钱。".format(threading.current_thread(),
                                                    money, gMoney))
            elif gTime >= gTotalTime:
                gLock.release()
                print("{}消费者准备消费{}元钱，剩余{}元钱，余额不足！！！".format(
                    threading.current_thread(), money, gMoney))
                break
            gLock.release()
            time.sleep(0.5)

def main():
    for x in range(3):
        t = Consumer(name="消费者线程{}".format(x))
        t.start()

    for x in range(5):
        t = Product(name="生产者线程{}".format(x))
        t.start()


if __name__ == '__main__':
    main()

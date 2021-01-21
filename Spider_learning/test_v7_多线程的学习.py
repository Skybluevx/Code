import time
import threading


class CodingThread(threading.Thread):
    def run(self):
        for x in range(5):
            print("正在写代码+{}".format(threading.current_thread()))
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for x in range(5):
            print("正在画画+{}".format(threading.current_thread()))
            time.sleep(1)


def main():
    t1 = CodingThread()
    t2 = DrawingThread()

    t1.start()
    t2.start()

    print(threading.enumerate())


if __name__ == '__main__':
    main()

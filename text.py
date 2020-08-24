import time
for i in range(5, 0, -1):
    print("\r倒计时{}秒！".format(i), end="", flush=True)
    time.sleep(1)
print("\r倒计时结束！")

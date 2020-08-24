import tqdm
import time


print("加载中...")
for i in tqdm(range(100), ncols=30):
    time.sleep(0.02)
    print

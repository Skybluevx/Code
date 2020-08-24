import tqdm
import time


def jingdutiao():
    print("加载中...")
    for i in tqdm(range(100), ncols=30):
        time.sleep(0.02)
        print("加载完毕...\n")


if __name__ == "__main__":
    jingdutiao()

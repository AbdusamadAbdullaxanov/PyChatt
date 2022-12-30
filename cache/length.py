import os

for i in os.listdir("D:/result/"):
    if os.path.getsize(f"D:/result/{i}") == 0:
        print(f"found {i}")
        os.remove(f"D:/result/{i}")

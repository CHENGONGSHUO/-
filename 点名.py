list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

import random
import os
import time

while 1:
    os.system("color 04")
    os.system("cls")
    result = random.choice(list0)
    print("· · ·")
    time.sleep(1)
    print(result)
    os.system("color 0a")
    loca = list0.index(result)
    del list0[loca]
    os.system("pause")
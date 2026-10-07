import time
for i in range(0,35):
    for j in range(34-i):
        print(" ",end="")

    for k in range(i):
        print(i,end=" ")
    time.sleep(0.1)

    print(i)              
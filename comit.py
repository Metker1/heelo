# Пузырьковый
import random
import time

def bubble(arr):
    n = len(arr)
    for i in  range(n):
        swapped = False

        for j in range(0,n - i -1):

            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True


        if not swapped:
            break




arr = []
for i in range(10000):
    arr.append(random.randint(1,10000))
start_time = time.time()
bubble(arr)
end_time = time.time()
elapsed = end_time - start_time
print(arr)
print(f'Затраченное время: {elapsed:.4f}')
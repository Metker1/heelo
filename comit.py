# Метод Шелла
import random
import time
def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i-inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc*5.0//11)

    return data
data = []
for i in range(10000):
    data.append(random.randint(1,10000))

start_time = time.time()
shell(data)
end_time = time.time()
elapsed = end_time - start_time
print(data)
print(f'Затраченное время: {elapsed:.4f}')
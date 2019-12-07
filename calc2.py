end_n = 18
max_time = 0
for i in range(1, end_n+1):
    time = 1.8 * 8 * i
    print("n={}: {}".format(i, time))
    max_time += time

for i in range(end_n+1, 50+1):
    time = 1.8 * 8 * end_n
    print("n={}: {}".format(i, time))
    max_time += time

print("max_time: {}".format(max_time))

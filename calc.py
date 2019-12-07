syoki_n = 10
start_n = 30
max_time = 1.8 * 8 * start_n * syoki_n
for i in range(1, 50+1 - start_n):
    time = 1.8 * 8 * (syoki_n+i)
    print("n={}: {}".format(start_n+i, time))
    max_time += time
print("max_time: {}".format(max_time))

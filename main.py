import urllib.request
import urllib.error
import time
import itertools
import copy


def query(url):
    res = urllib.request.urlopen(url=url)
    return res.read()


token = "JgEsWg7OxB5FDsie5tugjmYn72VN5KW9"

data = ['A', 'B', 'C', 'D']
ans_list = []
start = time.time()
"""
l = list(itertools.product(data, repeat=50))
for tup in l:
    s = "".join(tup)
    ans_list.append(s)
print("Time: {}".format(time.time() - start))
print("Element: {}", len(ans_list))
"""

max_point = 0
max_ans_list = []
for v1, v2 in itertools.product(data, repeat=2):
    ans = v1 + v2
    url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
    result = query(url)
    if max_point < int(result):
        max_point = int(result)
        max_ans_list = []
        max_ans_list.append(ans)
    elif max_point == int(result):
        max_ans_list.append(ans)

    print("{}: {}".format(ans, int(result)))
    time.sleep(1)

print("\n")
print("n=2")
print("max_ans_list: {}".format(max_ans_list))
print("max_point: {}".format(max_point))
print("\n")

temp_list = copy.copy(max_ans_list)
for n in range(3, 50+1):
    max_point = 0
    temp_list = copy.copy(max_ans_list)
    max_ans_list = []
    for v1, v2 in itertools.product(data, temp_list):
        ans = v1 + v2
        url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
        result = query(url)
        if max_point < int(result):
            max_point = int(result)
            max_ans_list = []
            max_ans_list.append(ans)
        elif max_point == int(result):
            max_ans_list.append(ans)

        print("{}: {}".format(ans, int(result)))
        time.sleep(1)

    for v1, v2 in itertools.product(temp_list, data):
        ans = v1 + v2
        url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
        result = query(url)
        if max_point < int(result):
            max_point = int(result)
            max_ans_list = []
            max_ans_list.append(ans)
        elif max_point == int(result):
            max_ans_list.append(ans)

        print("{}: {}".format(ans, int(result)))
        time.sleep(1)

    max_ans_list = copy.copy(list(set(max_ans_list)))

    print("\n")
    print("n={}".format(n))
    print("max_ans_list: {}".format(max_ans_list))
    print("max_point: {}".format(max_point))
    print("\n")

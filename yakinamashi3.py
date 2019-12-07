import urllib.request
import urllib.error
import time
import itertools
import copy


def query(url):
    res = urllib.request.urlopen(url=url)
    return res.read()


token = "ShbvMuwtldiC89s8aFHvwFZwzRhnkNRX"

data = ['A', 'B', 'C', 'D']
ans_list = []
start = time.time()

max_point = 0
max_ans_list = []
ans_dict = {}
for v1, v2 in itertools.product(data, repeat=2):
    ans = v1 + v2
    url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
    result = query(url)
    ans_dict[ans] = int(result)
    if max_point < int(result):
        max_point = int(result)

    print("{}: {}".format(ans, int(result)))
    time.sleep(1)

sort_dict_list = [key for key, value in sorted(
    ans_dict.items(), key=lambda x: -x[1])]

max_ans_list = copy.copy(sort_dict_list)

print("\n")
print("n=2")
print("max_ans_list: {}".format(max_ans_list))
print("max_point: {}".format(max_point))
print("\n")

first_len = 10
turning_point = 30
for n in range(3, turning_point+1):
    max_point = 0
    temp_list = copy.copy(max_ans_list)
    max_ans_list = []
    ans_dict = {}
    for v1, v2 in itertools.product(data, temp_list):
        ans = v1 + v2
        url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
        result = query(url)
        ans_dict[ans] = int(result)
        if max_point < int(result):
            max_point = int(result)

        print("{}: {}".format(ans, int(result)))
        time.sleep(1)

    for v1, v2 in itertools.product(temp_list, data):
        ans = v1 + v2
        url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
        result = query(url)
        ans_dict[ans] = int(result)

        print("{}: {}".format(ans, int(result)))
        time.sleep(1)

    sort_dict_list = [key for key, value in sorted(
        ans_dict.items(), key=lambda x: -x[1])]

    max_ans_list = copy.copy(sort_dict_list[:first_len])

    print("\n")
    print("n={}".format(n))
    print("max_ans_list: {}".format(max_ans_list))
    print("max_point: {}".format(max_point))
    print("\n")

for n in range(1, 50+1-turning_point):
    max_point = 0
    temp_list = copy.copy(max_ans_list)
    max_ans_list = []
    ans_dict = {}
    for v1, v2 in itertools.product(data, temp_list):
        ans = v1 + v2
        url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
        result = query(url)
        ans_dict[ans] = int(result)
        if max_point < int(result):
            max_point = int(result)

        print("{}: {}".format(ans, int(result)))
        time.sleep(1)

    for v1, v2 in itertools.product(temp_list, data):
        ans = v1 + v2
        url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
        result = query(url)
        ans_dict[ans] = int(result)

        print("{}: {}".format(ans, int(result)))
        time.sleep(1)

    sort_dict_list = [key for key, value in sorted(
        ans_dict.items(), key=lambda x: -x[1])]

    max_ans_list = copy.copy(sort_dict_list[:(first_len + n)])

    print("\n")
    print("n={}".format(turning_point+n))
    print("max_ans_list: {}".format(max_ans_list))
    print("max_point: {}".format(max_point))
    print("\n")

"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
call_time = {}
num = 0
while num < len(calls):
    # 往字典添加主叫号码键，不在字典就添加，在就加上时间
    if calls[num][0] not in call_time:
        call_time[calls[num][0]] = int(calls[num][3])
    else:
        call_time[calls[num][0]] += int(calls[num][3])
    # 往字典添加被叫号码键，不在字典就添加，在就加上时间
    if calls[num][1] not in call_time:
        call_time[calls[num][1]] = int(calls[num][3])
    else:
        call_time[calls[num][1]] += int(calls[num][3])
    num += 1
# 取得最大键值所对应的键
k = max(call_time, key=call_time.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(k, call_time[k]))

from collections import Counter
import operator
import csv
import re
import sys


data = sys.stdin.read()
result = re.findall('http.[^ ]+/new-homes/[\w-]+[^\d]/[\w-]+[^\d]/[\w-]+[^\d]/[\w-]+[^\d?$/]', data.lower())
pattern = re.compile('\w+\.lennar\.com')
m = set()
for each in result:
    m.add(pattern.search(each).group(0))
m = list(m)
lists = [[] for each in m]
print(m)
for each in result:
    lists[m.index(pattern.search(each).group(0))].append(re.search('/new-homes/.+', each).group(0))
for i in range(len(lists)):
    sorted_x = sorted(dict(Counter(lists[i])).items(), key=operator.itemgetter(1))
    sorted_x = sorted_x[-30:]
    with open(m[i]+'.csv', "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Path", "Count"])
        for item in sorted_x:
            csv_writer.writerow((item[0], item[1]))

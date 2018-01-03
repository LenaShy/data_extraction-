from collections import Counter
import operator
import csv
import re
import os

cn = []
pt = []
es = []
lists = [cn, pt, es]
names = ['Chinese.csv', 'Portuguese.csv', 'Spanish.csv']

print(os.getcwd())
lst = os.listdir('lennar/11')
for item in lst:
    lst2 = os.listdir('lennar/11/' + item)
    for each in lst2:
        my_file = open('lennar/11/' + item + '/' + each, 'r')
        pattern = re.compile(r'http.[^ ]+/new-homes/\D+/')
        result = pattern.findall(my_file.read().lower())
        for item2 in result:
            if item2.find('espanol.lennar') != -1: es.append(item2)
            if item2.find('cn.lennar') != -1: cn.append(item2)
            if item2.find('pt.lennar') != -1: pt.append(item2)

        my_file.close()
for i in range(3):
    sorted_x = sorted(dict(Counter(lists[i])).items(), key=operator.itemgetter(1))
    sorted_x =sorted_x[len(sorted_x)-30:]
    with open(names[i], "w") as file:
        csv_writer = csv.writer(file)

        for item in sorted_x:
            csv_writer.writerow((item[0], item[1]))
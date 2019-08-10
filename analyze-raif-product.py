# -*- coding: utf-8 -*-
from collections import defaultdict
import sys
filename = sys.argv[1]
all_descs = defaultdict(int)
money_sum = defaultdict(int)
currencies = defaultdict(str)
with open(filename, 'r') as f:
    first_line = True
    for line in f.read().decode('windows-1251').encode('utf8').strip().split('\n'):
        if not(first_line):
            description = line.split(';')[1]
            currency = line.split(';')[2]
            money = line.split(';')[3]
            if sum(letter >= 'а' and letter <= 'я' for letter in description) > 0 :
                all_descs[description] += 1
                money_sum[description] += float(money.replace(' ', ''))
                currencies[description] = currency;
        first_line = False
print("decription\tcount\ttotal_money")
print("\n".join('{desc}\t{count}\t{money} {currency}'.format(desc=v[1], count=v[0],
    money=money_sum[v[1]], currency=currencies[v[1]]) for v in sorted([(all_descs[k], k) for k in all_descs])))

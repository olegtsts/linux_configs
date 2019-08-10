# -*- coding: utf-8 -*-
from collections import defaultdict
import sys
filename = sys.argv[1]
all_descs = defaultdict(int)
with open(filename, 'r') as f:
    first_line = True
    for line in f.read().decode('windows-1251').encode('utf8').strip().split('\n'):
        description = line.split(';')[1]
        if sum(letter >= 'а' and letter <= 'я' for letter in description) > 0 and not(first_line):
            all_descs[description] += 1
        first_line = False
print("\n".join('{desc}\t{count}'.format(desc=v[1], count=v[0]) for v in sorted([(all_descs[k], k) for k in all_descs])))

# -*- coding: utf-8 -*-

import sys
filename = sys.argv[1]

with open("file2", 'r') as f:
    encodings=f.read().strip().split('\n')
print(encodings)

with open(filename, 'r') as f:
    sample = f.read()[:100]
    for encoding in encodings:
        print(encoding)
        try:
            print(sample.decode(encoding))
        except:
            print("failed")
            pass



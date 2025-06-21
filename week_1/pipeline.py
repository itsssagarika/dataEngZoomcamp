import sys

import pandas as pd

print(sys.argv)

filen = sys.argv[0]
day = sys.argv[1]
# some stuff with  pandas

print(f'job finished successfully for day = {day} file = {filen}')

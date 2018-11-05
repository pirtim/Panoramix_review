import itertools as it
from pprint import pprint

from org import fold_data as org
from new import fold_data as new
from new_rec import fold_data as rec
from new_rec_magic import fold_data as rec_magic
from test_data import d


strategies = [
    org,
    new,
    rec,
    rec_magic
]
data = d

results = {}
for s in strategies:
    results[s.__doc__] = {}

for i, (s, d) in enumerate(it.product(strategies, data)):
    results[s.__doc__][str(d)] = s(d)

    # print(i)
    # print(f'data: {d}')
    # print(f'strategy: {s.__doc__}')
    # print(s(d))



results_check = {}
for s in strategies:
    results_check[s.__doc__] = results[s.__doc__] == results['org']


pprint(results)
pprint(results_check)

print(all(results_check.values()))
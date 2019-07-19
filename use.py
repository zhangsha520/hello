# p = (4, 5)
# x, y = p
# s = 'hello'
# a, b, c, d, e = s
# print(a)

# record = ('dave', 'dave@example.com', '773-555', '847-555')
# name, email, *phone_number = record
# print(name)
# print(phone_number)

# sales_record = (1, 2, 3, 4, 5, 6, 7, 8, 5)
# *qtr, cur = sales_record
# avg = sum(qtr)/len(qtr)
# print(avg)

# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]

# def do_foo(x, y):
#     print('foo', x, y)

# def do_bar(s):
#     print('bar', s)

# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)

# line = 'nobody:*:-2:-2:unprivileged user:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname)
# print(homedir)
# print(sh)

# record = ('ACME', 50, 123.45, (12, 18, 2012))
# name, *_, (*_, year) = record
# print(name)
# print(year)

# items = [1, 10, 7, 4, 5, 9]
# head, *tail = items
# print(head)

# tail.append(12)
# print(tail)

# items = [1, 10, 7, 4, 5, 9]

# def sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head

# print(sum(items))

# from collections import deque

# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)

# import heapq

# nums = [1, 8, 2, 23, 7, -4, 28, 43, 37, 2]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))

# import heapq

# portfolio = [
#     {'name': 'ibm', 'shares': 100, 'price': 91.1},
#     {'name': 'aapl', 'shares': 50, 'price': 543.22},
#     {'name': 'fb', 'shares': 200, 'price': 21.09}
# ]

# cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
# print(cheap)

# expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
# print(expensive)

# import heapq
# nums = [1, 8, 2, 23, 7, -2, -4, 18, 23, 42, 37, 2]

# heap = list(nums)

# print(heap)

# heapq.heapify(heap)
# print(heap)
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))

# import heapq
# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0

#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         self._index +=1

#     def pop(self):
#         return heapq.heappop(self._queue)[-1]

# class Item:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return 'Item ({!r})'.format(self.name)

# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# q.push(Item('spam'), 4)
# q.push(Item('gork'), 1)
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())

# a = (1, Item('foo'))
# b = (5, Item('bar'))
# print(a < b)

# from collections import defaultdict
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)

# s = defaultdict(set)
# s['a'].add(1)
# s['a'].add(2)
# s['b'].add(4)

# print(s)
# print(d)

# d = {}
# d.setdefault('a', []).append(1)
# d.setdefault('a', []).append(2)
# print(d)

# d = defaultdict(list)
# for key, value in paris:
#     d[key].append(value)

# from collections import OrderedDict

# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['spam'] = 3
# d['gork'] = 4

# import json
# print(json.dumps(d))

# prices = {
#     'acme': 45.23,
#     'aapl': 612.78,
#     'ibm': 205.55,
#     'hpq': 37.20,
#     'fb': 10.75
# }

# min_price = min(zip(prices.values(), prices.keys()))
# print(min_price)

# max_price = max(zip(prices.values(), prices.keys()))
# print(max_price)

# prices_sorted = sorted(zip(prices.values(), prices.keys()))
# print(prices_sorted)

# a = {
#     'x': 1,
#     'y': 2,
#     'z': 3
# }

# b = {
#     'w': 10,
#     'x': 11,
#     'y': 2
# }

# print(a.keys() & b.keys())
# print(a.keys() - b.keys())
# print(a.items() & b.items())

# c = { key:a[key] for key in a.keys() - {'z', 'w'}}

# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)

# a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))

# items = [0, 1, 2, 3, 4, 5, 6]
# a = slice(2, 4)
# print(items[2:4])

# words = [
#     'look', 'into', 'my', 'eyes','look', 'into', 'my', 'eyes',
#     'the' , 'eyes', 'the', 'eyes', 'around', 'the', 'eyes', 'not',
#     'around', 'the', 'eyes', "don't", 'look', 'aroud', 'the', 'eyes'
#     ]

# from collections import Counter
# word_counts = Counter(words)
# top_three = word_counts.most_common(3)
# print(top_three)

rows = [
    {'address': '5412 N CLARK', 'DATE': '07/01/2012'},
    {'address': '5418 N CLARK', 'DATE': '07/04/2012'},
    {'address': '5800 E 58TH', 'DATE': '07/02/2012'},
    {'address': '2122 N CLARK', 'DATE': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'DATE': '07/02/2012'},
    {'address': '1060 W ADDSION', 'DATE': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'DATE': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'DATE': '07/04/2012'},
]

# from operator import itemgetter
# from itertools import groupby

# rows.sort(key=itemgetter('DATE'))

# for date, items in groupby(rows, key=itemgetter('DATE')):
#     print(date)
#     for i in items:
#         print('', i)

# from collections import defaultdict
# rows_by_date = defaultdict(list)
# for row in rows:
#     rows_by_date[row['DATE']].append(row)

# for r in rows_by_date['07/01/2012']:
#     print(r)

# mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# import math
# print([math.sqrt(n) for n in mylist if n > 0])
# clip_neg = [n if n > 0 else 0 for n in mylist]
# print(clip_neg)

# values = ['1', '2', '-3', '-', '4', 'N/A', '5']

# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False

# ivals = list(filter(is_int, values))
# print(ivals)

# mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# import math
# [math.sqrt(n) for n in mylist if n > 0]

# addresses = [
#     '5412 N CLARK',
#     '5148 N CLARK',
#     '5800 E 58TH',
#     '2122 N CLARK',
#     '5645 N RAVENSWOOD',
#     '1060 N ADDISON',
#     '4801 N BROADWAY',
#     '1039 W GRANVILLE'
# ]

# counts = [0, 3, 10, 4, 1, 7, 6, 1]
# from itertools import compress
# more5 = [ n > 5 for n in counts]
# print(more5)
# a = list(compress(addresses, more5))
# print(a)

# prices = {
#     'acme': 45.23,
#     'aapl': 612.78,
#     'ibm': 205.55,
#     'hpq': 37.20,
#     'fb': 10.75
# }

# p1 = { key: value for key, value in prices.items() if value > 200 }
# tech_names = {'aapl', 'ibm', 'hpq', 'msft'}
# p2 = {key: value for key, value in prices.items() if key in tech_names}
# print(p2)

# from collections import namedtuple
# subscriber = namedtuple('subscriber', ['addr', 'joined'])
# sub = subscriber('jonesy@example.com', '2012-10-19')
# print(sub)

# from collections import namedtuple

# Stock = namedtuple('stock', ['name', 'shares', 'price', 'date', 'time'])
# stock_prototype = Stock('', 0, 0.0, None, None)
# def dict_to_stock(s):
#     return stock_prototype._replace(**s)

# a = {'name': 'acme', 'shares': 100, 'price': 123.45}
# print(dict_to_stock(a))

# nums = [1, 2, 3, 4, 5]
# s = sum( x * x for x in nums)

# import os
# files = os.listdir('dirname')
# if any(name.endswitch('.py') for name in files):
#     print('there be python')
# else:
#     print('sorry, no python')

# s = ('acme', 50, 123.45)
# print(','.join(str(x) for x in s))

# portfolio = [
#     {'name': 'goog', 'shares': 50},
#     {'name': 'YHOO', 'shares': 75},
#     {'name': 'aol', 'shares': 20},
#     {'name': 'scox', 'shares': 65}
# ]

# min_shares = min(s['shares'] for s in portfolio)

# a = {'x': 1, 'z': 3}
# b = {'y': 2, 'z': 4}
# e = {'d': 4, 'e': 5}
# from collections import ChainMap

# c = ChainMap(a, b, e)
# print(c['x'])
# print(c['y'])
# print(c['z'])
# print(c['e'])

# line = 'asdf fjdk; afed, foo'
# import re
# fields = re.split(r'[;,\s]\s*', line)

# filename = 'spam.txt'
# filename.endswith('.txt')
# filename.startswith('file:')  # false
# url = 'http://www.python.org'
# url.startswith('http:')

# import os
# filenames = os.listdir('.')
# print(filenames)


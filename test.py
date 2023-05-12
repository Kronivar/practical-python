from collections import Counter, defaultdict

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

holdings = defaultdict(list)

for n, s, p in portfolio:
    holdings[n].append((s, p))
holdings['IBM']

def test():
    test = ['name', 'job', 'age']
    test2 = ['Christos', 'PM', 30]
    test3 = ['Evo', 'FA', 29]

    print(list(zip(test, test2, test3)))    
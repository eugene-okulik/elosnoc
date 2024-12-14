# def fib_seq(limit=100001):
#     count = 2
#     x = 0
#     num = 1
#     while count < limit:
#         num = x + num
#         x = num - x
#         count += 1
#         if count in [5, 200, 1000, 10000]:
#             yield num
#
#
# print(list(fib_seq(1000)))


def fib_seq(limit=100001):
    count = 2
    x = 0
    num = 1
    yield x
    yield num
    while count < limit:
        num = x + num
        yield num
        x = num - x
        count += 1


counter = 1
for number in fib_seq(100001):
    if counter in [5, 200, 1000, 10000]:
        print(number)
    counter += 1

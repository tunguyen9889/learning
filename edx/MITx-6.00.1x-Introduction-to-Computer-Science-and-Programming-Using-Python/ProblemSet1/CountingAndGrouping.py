from collections import Counter


def item_order(order):
    items = ('salad', 'hamburger', 'water')
    counter = Counter(order.split())
    return ' '.join(['{}:{}'.format(item, counter.get(item, 0)) for item in items])

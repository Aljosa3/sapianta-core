def simple_momentum(price):

    threshold = 100

    if price > threshold:
        return 1
    else:
        return -1

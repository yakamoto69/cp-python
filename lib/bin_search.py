def binary_search_monotonic_float(func, low, high, decr=False, times=100):
    for t in range(times):
        mid = (low + high) / 2

        if func(mid) ^ decr:
            high = mid
        else:
            low = mid

    return (low + high) / 2

def binary_search_monotonic(func, low, high, decr=False):
    if not decr:
        low -= 1
    else:
        high += 1
    while high - low > 1:
        mid = (low + high) // 2
        if func(mid) ^ decr:
            high = mid
        else:
            low = mid
    return high if not decr else low
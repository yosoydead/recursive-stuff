
def a(begin, end, step):
    if begin > end:
        return 0
    else:
        return a(begin + step, end, step) + begin


print(a(1,5,3))
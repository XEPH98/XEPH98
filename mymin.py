def my_min(x,*args):
    tutu = x, 999
    allt = tuple(tutu) + args
    return min(allt)

print(my_min(8,13,4,42,120,7))
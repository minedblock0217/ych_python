import math as m
def go_up(a, b,x):
    up_meter = a - b
    times = x / up_meter
    return times

times = m.ceil(go_up(10,3,50))

print(times)



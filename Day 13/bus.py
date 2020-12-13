import time
import math

#code from rosetta code
def chinese_remainder(n, a):
    sum = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def main():
    start = time.time()
    f = open("input.txt", "r")
    f = open("test.txt", "r")
    departure = int(f.readline())
    allServices = f.readline().strip().split(",")
    
    services = [int(word) for word in allServices if word.isdigit()]
    
    
    print(f"Reading took: {(time.time()-start)*1000:.2f}ms")

    start = time.time()
    part1Answer = part1(services, departure)
    print(f"Part 1 is : {part1Answer} {(time.time()-start)*1000:.2f}ms")
    start = time.time()
    part2Answer = part2(allServices)
    print(f"Part 2 is : {part2Answer} {(time.time()-start)*1000:.2f}ms")
    
def part1(services, departure):
    minWaiting = [departure, None]
    for bus in services:
        timeToWait = bus - departure%bus
        if timeToWait < minWaiting[0]:
            minWaiting = [timeToWait, bus]
    return minWaiting[0]*minWaiting[1]


def part2(allServices):
    allServices = [int(x) if not x == 'x' else None for x in allServices]
    timediff = []
    dct = []
    for (x, y) in enumerate(allServices):
        if not y == None:
            dct.append(y)
            timediff.append(y-x)
    return chinese_remainder(dct,timediff)
    

main()

sum = 0

for n in range(100001):
    sum += (-1)**n / (2*n+1)

pi = 4 * sum
print(pi)
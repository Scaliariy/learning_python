a = [(lambda x: x * x)(item) for item in range(1, 100, 3)]
# b = [a[ind](val) for ind, val in enumerate(range(1, 10)[::-1])]
print(a)

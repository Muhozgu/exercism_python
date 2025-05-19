def total():
    array = []
    for n in range(1, 65):
        array.append(2 ** (n - 1))
    print(sum(array))

total()
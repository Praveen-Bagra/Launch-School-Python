def mode(L):
    frequency = [0] * 10
    for i in L:
        print(i)
        frequency[i] = frequency[i] + 1
        print(frequency[i])
        print(frequency)
    for i in range(0, 10):
        print(max(frequency))
        if frequency[i]==max(frequency):
            return i

listA = [9,6,7,1,1,1,1]
mode(listA)
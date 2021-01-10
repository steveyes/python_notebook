def firstn(n):
    num = 0
    while num < n:
        # return as a generator
        yield num
        num += 1


print(type(firstn))
print(type(firstn(100)))
sum_of_first_n = sum(firstn(100))
print(sum_of_first_n)


def firstm(m):
    # return a generator
    return (num for num in range(0, m))


print(type(firstm))
print(type(firstm(100)))
sum_of_first_n = sum(firstm(100))
print(sum_of_first_n)

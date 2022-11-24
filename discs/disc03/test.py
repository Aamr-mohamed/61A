x = 9 % 2
print(x)
for i in range(2, 10):
    print(i)


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
        else:
            print("ya fa4el ya m3ras")


print(is_prime(9))

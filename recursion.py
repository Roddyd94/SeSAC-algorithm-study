system_cnt = 0


def countdown(n):
    global system_cnt
    system_cnt += 1
    if n == 0:
        return

    print(n)
    countdown(n - 1)


arr = [0] * 21
arr[0] = 1
arr[1] = 1


def fibonacci0(n):
    global system_cnt
    system_cnt += 1
    if n == 0 or n == 1:
        return 1

    return fibonacci0(n - 2) + fibonacci0(n - 1)


def fibonacci1(n):
    global system_cnt
    system_cnt += 1
    if arr[n]:
        return arr[n]

    arr[n] = fibonacci1(n - 2) + fibonacci1(n - 1)
    return arr[n]


def factorial(n):
    global system_cnt
    system_cnt += 1
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(fibonacci0(20))
print(system_cnt)
system_cnt = 0
print(fibonacci1(20))
print(system_cnt)

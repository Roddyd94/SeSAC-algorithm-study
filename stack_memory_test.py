def count_and_call_self(n):
    print(n)
    count_and_call_self(n + 1)


count_and_call_self(1)

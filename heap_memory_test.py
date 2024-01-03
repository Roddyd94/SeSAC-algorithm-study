def put_to_list_and_count():
    cnt = 1
    while True:
        l.append(cnt)
        if cnt % 1_000_000 == 0:
            print(cnt)
        if cnt % 1_000_000_000 == 0:
            print(*l)
            break
        cnt += 1


l = []

put_to_list_and_count()

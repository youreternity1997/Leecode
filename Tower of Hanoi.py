def hanoi(n, A, B, C):
    if n == 1:
        return [(A, C)]
    else:
        return hanoi(n-1, A, C, B) + hanoi(1, A, B, C) + hanoi(n-1, B, A, C)


n = input("Please enter integer:")
for move in hanoi(int(n), 'A', 'B', 'C'):
    print("move %c to %c" % move)
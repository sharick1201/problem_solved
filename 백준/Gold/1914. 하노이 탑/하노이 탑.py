def hanoi(depth, frm, via, to):
    if depth == 1:
        mv_lst.append((frm, to))
        return

    # n-1개를 경유지로 옮겨둔다
    hanoi(depth - 1, frm, to, via)

    # n번 원판을 옮긴다
    mv_lst.append((frm, to))

    # n-1개를 경유지에서 다시 도착지로
    hanoi(depth - 1, via, frm, to)


def large_hanoi(depth):
    if depth == 1:
        return 1
    return 2 * large_hanoi(depth - 1) + 1

N = int(input())
mv_lst = []

if N <= 20:
    hanoi(N, 1, 2, 3)
    print(len(mv_lst))
    for i in range(len(mv_lst)):
        print(mv_lst[i][0], mv_lst[i][1])
else:
    print(large_hanoi(N))
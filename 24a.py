DI = [0, -1, 0, 1]
DJ = [1, 0, -1, 0]

INF = 10 ** 18

R = 27
C = 122
TIME_LIMIT = 5000

grid = [input() for _ in range(R)]

blizzards = [[] for _ in range(TIME_LIMIT)]
blizzards_no_d = [set([]) for _ in range(TIME_LIMIT)]

for i in range(R):
    for j in range(C):
        if grid[i][j] != '#' and grid[i][j] != '.':
            blizzards[0].append((i, j, ">^<v".index(grid[i][j])))
            blizzards_no_d[0].add((i, j))


def within(i, j):
    return 1 <= i <= R - 2 and 1 <= j <= C - 2 or (i, j) == (0, 1) or (i, j) == (R - 1, C - 2)


for t in range(1, TIME_LIMIT):
    previous = blizzards[t - 1]
    for i, j, d in previous:
        i_to, j_to = i + DI[d], j + DJ[d]
        if not within(i_to, j_to):
            i_to = (i_to + 2 * DI[d]) % R
            j_to = (j_to + 2 * DJ[d]) % C
        blizzards[t].append((i_to, j_to, d))
        blizzards_no_d[t].add((i_to, j_to))

reachable = [[False for _ in range(C)] for _ in range(R)]
reachable[0][1] = True

for t in range(1, TIME_LIMIT - 1):
    new_reachable = [[False for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if not within(i, j) or not reachable[i][j]:
                continue
            for d in range(4):
                i_to, j_to = i + DI[d], j + DJ[d]
                if not within(i_to, j_to):
                    continue
                if (i_to, j_to) not in blizzards_no_d[t]:
                    new_reachable[i_to][j_to] = True
            if (i, j) not in blizzards_no_d[t]:
                new_reachable[i][j] = True
    reachable = new_reachable
    if reachable[R - 1][C - 2]:
        print(t)
        exit()

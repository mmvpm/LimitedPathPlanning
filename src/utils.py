inf = 10 ** 9

uldr = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def compute_cost(s, t):
    return ( abs(s.i - t.i) ** 2 + abs(s.j - t.j) ** 2 ) ** 0.5


# def heuristic(s, t):
#     di = abs(s.i - t.i)
#     dj = abs(s.j - t.j)
#     return abs(di - dj) + 2 ** 0.5 * min(di, dj)

def heuristic(s, t):
    return min(abs(s.i - t.i), abs(s.j - t.j))

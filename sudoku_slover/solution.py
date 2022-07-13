availeble_vals = set(range(1, 10))


def sudoku(puzzle):
    queue_items = [puzzle]
    while queue_items:
        item = queue_items.pop(0)
        for x in range(len(puzzle)):
            for y in range(len(puzzle[x])):
                if not item[x][y]:
                    imp = get_impossible_values(item, x, y)
                    cur_avail = availeble_vals - imp
                    if len(cur_avail) == 1:
                        item[x][y] = next(iter(cur_avail))
                        queue_items.append(item)
    return puzzle


def get_impossible_values(item, x, y):
    res = set()
    sqr = (x // 3 + 1, y // 3 + 1)
    for i in item[x]:
        if i:
            res.add(i)
    for i in range(len(item)):
        if item[i][y]:
            res.add(item[i][y])
    for x in range(sqr[0] * 3 - 3, sqr[0] * 3):
        for y in range(sqr[1] * 3 - 3, sqr[1] * 3):
            res.add(item[x][y])
    return res


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
sudoku(puzzle)

def path_finder(maze):
    maze = maze.split('\n')
    maze = [[z for z in i] for i in maze]
    el_queue = [(0, 0)]
    already_look = set()
    finish = (len(maze) - 1, len(maze[0]) - 1)
    if len(maze) == 1:
        return True
    while el_queue:
        v = el_queue[0]
        vals = (
            (v[0] + 1, v[1]),
            (v[0] - 1, v[1]),
            (v[0], v[1] + 1),
            (v[0], v[1] - 1),
        )
        for cur_val in vals:
            if (cur_val[0] < 0 or cur_val[1] < 0) or (cur_val[0] > finish[0] or cur_val[1] > finish[1]):
                continue
            if cur_val == finish:
                return True
            elif maze[cur_val[0]][cur_val[1]] != "W" and cur_val not in el_queue and cur_val not in already_look:
                el_queue.append(cur_val)
            else:
                continue
        already_look.add(v)
        el_queue.pop(0)
    return False

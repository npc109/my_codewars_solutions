def solution(n: int):
    res_list = [int(i) for i in str(n)]
    max_value = max(res_list)
    breakable = False
    cur_top_index = None
    res_index = None
    for ind, val in enumerate(res_list[::-1], start=1):
        if val is max_value:
            continue
        cur_top_index = len(res_list) - ind
        print(cur_top_index)
        if cur_top_index > 0:
            for cur_ind, cur_val in enumerate(res_list[cur_top_index - 1::-1], start=1):
                bot_index = cur_top_index - cur_ind
                if cur_val > val:
                    res_index = bot_index

                    res_list[cur_top_index], res_list[bot_index] = cur_val, val
                    print(cur_top_index, bot_index, "INDEXES", res_list)
                    breakable = True
                    break
        if breakable:
            break
    if res_index is None:
        return -1
    sortable = res_list[res_index:cur_top_index + 1]
    print(res_index, cur_top_index + 1, res_list)
    if len(sortable) > 1:
        sortable.sort()
        print(sortable, "SORTABLE")
        sortable.reverse()
        res = res_list[res_index:cur_top_index + 1:] + sortable
    else:
        res = res_list
    if res[0] == 0:
        return -1
    res = int("".join(str(i) for i in res))
    return res


if __name__ == "__main__":
    print(solution(1207), 1207)

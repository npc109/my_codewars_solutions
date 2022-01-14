def snail(snail_map, result=None):
    if not result:
        result = []
    if snail_map and snail_map[0]:
        result += snail_map[0][:-1:]
        for i in snail_map:
            result.append(i[-1])
        for zxc in snail_map[-1][-2::-1]:
            result.append(zxc)
        for i in snail_map[-2:0:-1]:
            result.append(i[0])
        try:
            snail_map.pop(0)
            snail_map.pop(-1)
        except:
            return result
        for i in snail_map:
            try:
                i.pop(0)
                i.pop(-1)
            except:
                return result
        return snail(snail_map, result)
    else:
        return result

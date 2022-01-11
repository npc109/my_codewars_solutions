nums_pool = [1]
cache_values = []


def get_two_gen():
    for num in nums_pool:
        yield num * 2


def get_three_gen():
    for num in nums_pool:
        yield num * 3


def get_five_gen():
    for num in nums_pool:
        yield num * 5


two_gen = get_two_gen()
three_gen = get_three_gen()
five_gen = get_five_gen()


def solution(n: int) -> int:
    global nums_pool
    global cache_values
    if len(nums_pool) > n - 1:
        return nums_pool[n - 1]
    vls = {2: two_gen, 3: three_gen, 5: five_gen}
    while len(nums_pool) < n:
        if not cache_values:
            new_two = [2, next(two_gen)]
            new_three = [3, next(three_gen)]
            new_five = [5, next(five_gen)]
            res = [new_two, new_three, new_five]
            res.sort(key=lambda x: x[1])
            min_val = res[0]
            nums_pool.append(min_val[1])
            cache_values.append(res[1])
            cache_values.append(res[2])
        else:
            min_cache_val = cache_values[0][1]
            mults = [cache_val[0] for cache_val in cache_values]
            for val in vls:
                if val not in mults:
                    new_min_val = [val, next(vls[val])]
            if new_min_val[1] < min_cache_val and new_min_val[1] not in nums_pool:
                nums_pool.append(new_min_val[1])
            else:
                if min_cache_val not in nums_pool:
                    nums_pool.append(min_cache_val)
                cache_values.pop(0)
                cache_values.append(new_min_val)
                cache_values.sort(key=lambda x: x[1])
    return nums_pool[n - 1]


if __name__ == "__main__":
    for i in range(51):
        print(solution(i))

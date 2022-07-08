def minus(value, revers_new):
    if value[-2] == 5:
        return value[-1]
    if value[-1] < 5 and value[-2] != 5:
        for i in range(1, len(value)):
            if revers_new[i] > 0:
                value[-i] -= 1
                revers_new[i] -= 1
                break


def solution(start, end):

    garanty_count = end // 10



if __name__ == '__main__':
    print(solution(0, 100))

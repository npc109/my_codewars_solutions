def _rolldice_sum_prob(sum_, dice_amount, count=0):
    if sum_ == 0 and dice_amount == 0 or dice_amount == 1 and sum_ <= 6:
        return 1
    elif dice_amount * 6 < sum_ < dice_amount:
        return None
    for i in range(1, 7):
        if sum_ - i > 0 and dice_amount - 1 > 0:
            count += _rolldice_sum_prob(sum_ - i, dice_amount - 1)
    return count


def rolldice_sum_prob(sum_, dice_amount):
    if dice_amount * 6 < sum_ or sum_ < dice_amount:
        print("Sum must be between {} and {}".format(dice_amount, dice_amount * 6))
        return 0
    elif sum_ == dice_amount or sum_ == dice_amount * 6:
        return 1 / (6 ** dice_amount)
    else:
        return _rolldice_sum_prob(sum_, dice_amount) / (6 ** dice_amount)


if __name__ == "__main__":
    print(rolldice_sum_prob(22, 3))

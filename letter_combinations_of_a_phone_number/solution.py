literals = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def solution(digits: str, val="", data=None):
    if data is None:
        data = []
    if not digits and val:
        data.append(val)
    for i, v in enumerate(digits):
        for l in literals[v]:
            solution(digits[i + 1::], f'{val}{l}', data)
        break
    return data

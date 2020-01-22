def slide(line):
    non_zeros = [num for num in line if num > 0]
    zeros = [num for num in line if num == 0]
    return non_zeros + zeros


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line = slide(line)
    for i in range(len(line) - 1):
        x = line[i]
        y = line[i + 1]
        if x == y:
            line[i] *= 2
            line[i + 1] = 0
    return slide(line)


if __name__ == '__main__':
    print(merge([2, 0, 2, 2]))  # [4,2,0,0]
    print(merge([4, 4, 8, 16]))  # [8, 8, 16, 0]
    print(merge([8, 8, 16, 0]))  # [16, 16, 0, 0]
    print(merge([16, 16, 0, 0]))  # [32, 0, 0, 0]

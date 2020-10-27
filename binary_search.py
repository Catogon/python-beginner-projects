from random import sample


def binary_search(list_, target):
    left, right = 0, len(list_) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_[middle] < target:
            # Eliminate the left half of the list
            left = middle + 1
        elif list_[middle] > target:
            # Eliminate the right half of the list
            right = middle - 1
        else:
            return middle   # return the index of target
    return


if __name__ == "__main__":
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))

    try:
        target = int(input('Pick a number between 0-100: '))
        target_index = binary_search(rand_list, target)

        print(f'List: {rand_list}')
        if target_index is not None:
            print(f'Found {target} in index {target_index}')
        else:
            print(f'Cannot find {target} in the list')
    except ValueError:
        print('Invalid input')
